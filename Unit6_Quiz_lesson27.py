# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(input_text):
    final_list = []
    newtext = ''
    i = 0
    begin = False
    end = False
    for chr in input_text:
        if chr == '<':
            begin = True
        if chr == '>':
            end = True
            newtext = newtext + ' '
        if not begin and not end:
            newtext = newtext + chr
            begin = False
            end = False
        if begin and end:
            begin = False
            end = False
    return newtext.split()

def remove_tags2(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + " " + string[end + 1:]
        start = string.find('<')
    return string.split()    
 
    
print '----------------------------------------------'
print '----- REMOVE TAGS ----------------------------'
print '----------------------------------------------'

print remove_tags2('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(list, date):
    newdate = ''
    month = date[0:date.find('/')]
    day = date[date.find('/')+1:]
    day = day[0:day.find('/')]
    year = date[date.find('/')+1:]
    year = year[year.find('/')+1:]
    day + ' ' + list[int(month)] + ' ' + year 
    return day + ' ' + list[int(month)] + ' ' + year 
    
    
def date_converter2(list,date):
    month, day, year = date.split('/')
    return day + ' ' + list[int(month)] + ' ' + year   
        
print '----------------------------------------------'
print '----- Date Converter -------------------------'
print '----------------------------------------------'

print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/8/1791')
#>>> 5 december 1791

print '----------------------------------------------'
print '----- Date Converter2 - Using Split with "/"  '
print '----------------------------------------------'

print date_converter2(english, '5/11/2012')
#>>> 11 May 2012

print date_converter2(english, '5/11/12')
#>>> 11 May 12

print date_converter2(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter2(swedish, '12/8/1791')

#>>> 5 december 1791
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.
source = 'text'
print source.replace(source[1:3],'what')

def make_converter(match, replacement):
    return match + '#' + replacement
    



def apply_converter(converter, string):
    match = converter[0:converter.find('#')]
    replace = converter[converter.find('#')+1:]
    while True:
        if match in string:
            start = string.find(match)
            end = start + len(match)
            string = string.replace(string[start:end],replace)
        else:  
            return string
    
print '----------------------------------------------'
print '----- String Converter -----------------------'
print '----------------------------------------------'

# For example,

c1 = make_converter('a', '2')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

print '----------------------------------------------'
print '----- longest repetition ---------------------'
print '----------------------------------------------'

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list):
    tally = {}
    previous = ""
    if len(list) > 0:
        # Start counting until something new value found
        for element in list:
            if element != previous:
                count = 1
                previous = element
            else:
                count = count + 1
            # check the maximum count of value
            # if already showed up in list somewhere
            if element in tally:
                if count > tally[element]:
                    tally[element] = count
            else:
                tally[element] = 1
        base = 0     
        for element in tally:
            if tally[element] > base:
                base, greatest = tally[element], element
        return greatest
    else:
        return None
            
        #return greatest

        



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print '----------------------------------------------'
print '----- Deep Reverse       ---------------------'
print '----------------------------------------------'

# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(list):
    print "STILL NEED TO WORK THIS ONE"



#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]

