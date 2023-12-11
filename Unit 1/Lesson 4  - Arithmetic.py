# Just treat booleans as integers in arithmetic

print(True + 2) # boolean + int = int (remember that booleans are kinda integers
print(True + 2.5) # boolean + float = float (just treat booleans as int)
print(True + True) # boolean + boolean = int

# Division
# In divisions, literally every answer is a float. This is because the computer
# Goes through long division (like step by step) when doing divisions.
# For the computer, 4/2 is 2.00000000000000 (until it runs out of memory size)
# And when it prints the answer, it removes all the zeroes except for the first

# print(5/False)  <- note that false is equal to zero so this will return error

print(0**0) # <- this will print 1
print(0.0**0) # <- this prints 1.0

print(57.9%4)
print(17%3.2)
print(32.5%3.2)
print("")
# double slash // prints ONLY the quotient (and it can be a float)
print(5//2)
print(74.3 // 2)
