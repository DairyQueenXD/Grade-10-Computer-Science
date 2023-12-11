# Built-in String Functions
s = "Apple Pie!"
print(len(s))

#1 - .upper() <- turns alphabet into all upper case letters
print(s.upper())

#2 - .lower() <- turns alphabet into all lower case letters
print(s.lower())

## Note that the built-in functions do NOT alter the original string
## You have to reassign to alter the original string, like:
## s = s.lower()

#3 - .find(substring) <- locates the FIRST position of the substring 
# in the original string. If the substring doesn't exist
# then -1 will be returned
print(s.find("e"))

#4 - .rfind(substring) <- locates the LAST position of the substring in
# the original string. If substring doesn't exist it returns -1
print(s.rfind("e"))  # returns 8
print(s.rfind("l")) # returns 3
print(s.rfind("Pi")) # returns 6 < note that it still returns the positon of the
# first character of the substring (in this case, P)

#5 - .isalpha() <- returns True if the string contains only alphabets
print(s.isalpha()) # False because of the spaces and exclamation mark
t = "123apple"
print(t.isalpha()) # False because of the numbers
u = "aPpLeJeLlYTIME"
print(u.isalpha()) # True

#6 - .isdigit() <- returns True if the string only contains digits
v = "1234"
print(v.isdigit()) # True
w = "00000000000000000012300000000000"
print(w.isdigit()) # True
x = "239129039 "
print(x.isdigit()) # False
y = "-123" 
print(y.isdigit()) # False because there is a '-'
z = "3.14"
print(z.isdigit()) # False because there is a point ('.')

"""
Example 1: Ask the user for 5 strings. After each entry, return one of the following:
1. The character 's' exists in the string
2. The character 's' does not exist in the string
"""

for i in range(5):
    s1 = input("Enter a string #" + str(i+1) + ": ")
    if s1.find('s') != -1:
        print("The character \'s\' exists in " + s1)
    else:
        print("The character \'s\' does not exist in " + s1)

"""
Example 2: Ask the user for 1 string. The computer will display the sum of all
digits in the string
"""

s2 = input("Enter a string: ")
acc = 0
for i in range(len(s2)):
    if s2[i].isdigit():
        acc += int(s2[i])
print(acc)
