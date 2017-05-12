# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)





print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800

# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == "":
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
# another way to do it with for loops
# although less elegent, in Python this is 
# more efficient.    It took the instructor
# 3 tries to get this code to work properly.
def iter_palindrome(s):
    for i in range(0,len(s)/2):
        if s[i] != s[-(i + 1)]:
            return False
    return True
 
 
print '----- RECURSIVE METHOD -----' 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
print is_palindrome('abcdedcba')
print '----- ITERATIVE METHOD -----'
print iter_palindrome('')
#>>> True
print iter_palindrome('abab')
#>>> False
print iter_palindrome('abba')
#>>> True
print iter_palindrome('abcdedcba')

# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)
print '----- fibonacci Recursive -----'

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci (n-2))

print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610

print '----- fibonacci Iterative -----'
# Fibo series   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# Fibo number   0, 1, 2, 3, 4, 5, 6, 7,  8,   9, 10

def iter_fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

        
print iter_fibonacci(0)
#>>> 0
print iter_fibonacci(1)
#>>> 1
print iter_fibonacci(15)
#>>> 610        
print '-------  Mass of Bunnies to End the World ----'      
mass_of_earth = 5.9722 * 10**24 # Kilogram estimate
mass_of_rabbit = 2 # kilograms

n=1
while iter_fibonacci(n) * mass_of_rabbit < mass_of_earth:
    n = n + 1
print 'The number of months of the mass of rabbits to equal'
print 'the mass of the earth'
print n, 'months and it would be', iter_fibonacci(n), 'rabbits'     
   
   






