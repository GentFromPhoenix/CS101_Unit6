# Wanted to add a comment line up here and see if can push up to GitHub

# Modify the crawl_web procedure so that instead of just returning the 
# index, it returns an index and a graph. The graph should be a 
# Dictionary where the key:value entries are:

#  url: [list of pages url links to] 


def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipes:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbanzo beans.
<li> Crush them in a blender.
<li> Add 3 tablespoons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        return None
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, ranks, keyword):
    bestrank = 0
    bestpage = ''
    if keyword in index:
        for element in index[keyword]:
            if ranks[element] > bestrank:
                bestrank = ranks[element]
                bestpage = element
        return bestpage
    return None        

# This is "lookup" that is sorted
def ordered_search(index, ranks, keyword): 
    array = index[keyword]
    array_pass = []
    # Define List to sort [url1,rank],[url2,rank]...
    for element in array:
        array_pass.append([element,ranks[element]])
    # Sort the above list in procedure sort
    sorted_ranks =  sort(array_pass)
    # create final list to pass back based on sorted list url elements
    array_pass = []
    for element in sorted_ranks:
        array_pass.append(element[0])          
    return array_pass          
           
           
def sort(array):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0][1]
        for x in array:
            if x[1] < pivot:
                less.append(x)
            if x[1] == pivot:
                equal.append(x)
            if x[1] > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(greater)+equal+sort(less)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array              

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10 
    ranks = {}
    npages = len(graph)
    # this loop initializes the rankings dictionary.
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node]) / len(graph[node])      
            newranks[page] = newrank
        ranks = newranks
        #print 'loop', i
    return ranks
    
  


index , graph = crawl_web('http://udacity.com/cs101x/urank/index.html') 

#if 'http://udacity.com/cs101x/urank/index.html' in graph:
#    print graph['http://udacity.com/cs101x/urank/index.html']
#>>> ['http://udacity.com/cs101x/urank/hummus.html',
#'http://udacity.com/cs101x/urank/arsenic.html',
#'http://udacity.com/cs101x/urank/kathleen.html',
#'http://udacity.com/cs101x/urank/nickel.html',
#'http://udacity.com/cs101x/urank/zinc.html']
print '--------------------------------------------------------'
print '------             RANKING PAGES -----------------------'
print '--------------------------------------------------------'

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print 'The ranks are'
print ranks
#print index

#>>> {'http://udacity.com/cs101x/urank/kathleen.html': 0.11661866666666663,
#'http://udacity.com/cs101x/urank/zinc.html': 0.038666666666666655,
#'http://udacity.com/cs101x/urank/hummus.html': 0.038666666666666655,
#'http://udacity.com/cs101x/urank/arsenic.html': 0.054133333333333325,
#'http://udacity.com/cs101x/urank/index.html': 0.033333333333333326,
#'http://udacity.com/cs101x/urank/nickel.html': 0.09743999999999997}
print '--------------------------------------------------------'
print '------     Picking the best page -----------------------'
print '--------------------------------------------------------'

print '--------------------' 
print lookup(index, ranks, 'The')
print lookup(index, ranks, 'Hummus')
#>>> http://udacity.com/cs101x/urank/kathleen.html

print lookup(index, ranks, 'the')
#>>> http://udacity.com/cs101x/urank/nickel.html

print lookup(index, ranks, 'babaganoush')
#>>> None
print '------------------------------------------'
print '------ Ordering Search Results  ----------'
print '------------------------------------------'
print '---Keyword --- "Hummus"'
print ordered_search(index, ranks, 'Hummus')
#>>> ['http://udacity.com/cs101x/urank/kathleen.html',
#    'http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']
print '---Keyword --- "the"'
print ordered_search(index, ranks, 'the')
#>>> ['http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']


#print ordered_search(index, ranks, 'babaganoush')
#>>> None
