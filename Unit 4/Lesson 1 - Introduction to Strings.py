## There is a lot more to strings than just simply storing a bunch of characters

s = "Hello Chow!"

"""
Indexing: 
Every character has a positon / index starting with 0
The space is also a character

Negative Indexing : 
Last characer of a string is position -1

Substring = string contained within another string
Ex: "ello", "Ch", "Hello Chow!", "w!", "", " " are substrings of "Hello Chow!"

We can obtain a substring from the original string using slicing.
"""
print(s[1:5])
print(s[6:8])
print(s[6:7])
print(s[-5:-1])
print(s[6:100]) # Even though it exceeds, the computer just stops at the last character
print(s[-10:4]) # This prints "ell " cuz position -10 exists
print(s[-3:3]) # This will just print an empty string because the computer expects -2, -1
print(s[5:-3]) # This prints " Ch" cuz the position -3 exists
print(s[8:-5]) # This will print an empty string

# Special Slicing
print(s[6:]) # This prints from position 6 to the end ("Chow!")
print(s[:8]) # This prints everything until position 7 (including)

## Different ways to crash the program
# s[100] <- The index is out of range so crash
# s[-12] <- Index out of range
