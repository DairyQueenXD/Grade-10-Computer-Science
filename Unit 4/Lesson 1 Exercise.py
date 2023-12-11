#[String1.py] Write a program that asks the user for a string. 
#The program will then display every other letter of the string.
#e.g. if the input is “Hello Markville”, the output will be “HloMrvle”

s1 = input("Enter a string: ")
for i in range(0, len(s1), 2):
    print(s1[i], end = "")

print("")

"""
[String2.py] Write a program that asks the user for a string. 
The program will display a string with “*” added in between all characters.
e.g. If the input is “Hello ICS2O”, the output will be “*H*e*l*l*o* *I*C*S*2*O*”
"""
s2 = input("Enter a string: ")
for i in range(len(s2)):
    print(s2[i], end="*")

print("")

"""
[String3.py] Write a program that asks the user for two strings. 
The program will display alternating letters from the two strings
until one of the two strings run out of characters.
e.g. If the inputs are “Markville” and “School”, the output will be “MSacrhkovoil”
"""
s3 = input("Enter a string: ")
s4 = input("Enter a string: ")
smaller = s3
if len(s3) > len(s4):
    for i in range(len(s3)):
        print(s4[i]+s3[i],end="")   
else:
    for i in range(len(s4)):
        print(s3[i]+s4[i],end="")

"""
[String4.py] Write a program that asks the user for a string and a character. 
The program will display the index of the first occurrence of the character located in the string.
Return -1 if the character does not exist in the string.

e.g. If the inputs are “Markville” and “v”, the output will be 4
e.g. If the inputs are“Markville” and “l”, the output will be 6
e.g. If the inputs are“Markville” and “C”, the output will be -1
"""
print("")
s5 = input("Enter a string: ")
s6 = input("Enter a character: ")
for i in range(len(s5)):
    if s5[i] == s6:
        print(i)
