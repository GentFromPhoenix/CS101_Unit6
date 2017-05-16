# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
    # what is the baseline
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result = result + ancestors(genealogy, parent)
        return result
    return []





# Here are some examples:
print '------------------------------------------'
print '----          Ancestors        -----------'
print '------------------------------------------'
print ancestors(ada_family, 'Augusta Ada King')
print ''
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

#print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

#print ancestors(ada_family, 'Dave')
#>>> []

# ----------------------------------------------------------------------
# Double Gold Star
# ----------------------------------------------------------------------

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

print '------------------------------------------'
print '----  Blaise Pascal Triangle   -----------'
print '------------------------------------------'
def triangle(n):
    if n == 0:
        return []
    previous = [0]
    result = [[1]]  
    for loop in range(1,n):
        current = [1]
        previous.append(1)
        for i in range(1,loop):
            current.append(previous[i] + previous[i+1])
        for i in range(1,loop):
            previous[i+1] = current[i]
        current.append(1)
        result.append(current)
    return result
            
# There answer was this way
# more elegent obviously - still not thinking in 
# that "make separate procedure mode"

def triangle2(n):
    result = []
    current = [1] 
    for unused in range(0,n):
        result.append(current) 
        current = make_next_row(current) 
    return result    
 
def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result       
        
        
        



print triangle2(0)
#>>> []

print triangle2(1)
#>>> [[1]]

print triangle2(2)
#>> [[1], [1, 1]]

print triangle2(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle2(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]



