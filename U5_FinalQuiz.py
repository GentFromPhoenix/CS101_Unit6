# Unit 5 Follow on Question --

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary.  For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    dates = []
    for element in courses:
        if course in courses[element]:
            dates.append(element)   
    return dates   

# [Double Gold Star] Define a procedure, involved(courses, person), that takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester (the courses in the list 
# can be in any order).


def involved(course, person):
    involved = {}
    for element in courses:
        for c in courses[element]:
            for detail in courses[element][c]:
                if person == courses[element][c][detail]:
                    if element in involved:
                        #print 'TRUE', detail, course[element][c][detail]
                        involved[element] = involved[element] + [c]
                    else:
                        involved[element] = [c]
    return involved   

#print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']

#print when_offered(courses, 'bio893')
#>>> []

print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print 'Peter C.', involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print 'Dorina', involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

print 'Peter', involved(courses,'Peter')
#>>> {}

print 'Robotic', involved(courses,'Robotic')
#>>> {}

print 'null', involved(courses, '')
#>>> {}