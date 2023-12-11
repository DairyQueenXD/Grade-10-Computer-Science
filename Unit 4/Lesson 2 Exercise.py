## Number 5
s1 = input("Enter a string: ")
digits = 0
letters = 0
for i in range(len(s1)):
    if s1[i].isdigit():
        digits += 1
    if s1[i].isalpha():
        letters += 1
print("Number of digits: " + str(digits))
print("Number of letters " + str(letters))

## Number 6
s = input("Enter a string: ")
counter = 0
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        counter += 1
print(counter)
