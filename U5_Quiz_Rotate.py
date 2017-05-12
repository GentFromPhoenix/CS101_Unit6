# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    if n >= 0 and n > ord('z') - ord(letter):
        return chr(ord('a') + (n - (ord('z') - ord(letter) + 1)))
    if n < 0 and n < ord('a') - ord(letter):
        return chr(ord('z') + (n - (ord('a') - ord(letter) - 1)))
    return chr(ord(letter) + n)



def rotate(code, n):
    result = ""
    for e in code:
        if e == " ":
            result = result + " "
        else:
            result = result + shift_n_letters(e, n)
    return result
            
    # Your code here





print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???

string = 'wonderful'
print string[1:-2]