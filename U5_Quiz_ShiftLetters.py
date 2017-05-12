# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.


def shift(letter):
    if letter == 'z':
        return 'a'
    else:
        return chr(ord(letter) + 1)

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if n >= 0 and n > ord('z') - ord(letter):
        return chr(ord('a') + (n - (ord('z') - ord(letter) + 1)))
    if n < 0 and n < ord('a') - ord(letter):
        return chr(ord('z') + (n - (ord('a') - ord(letter) - 1)))
    return chr(ord(letter) + n)
       
        


print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('h', -20)
#>>> x