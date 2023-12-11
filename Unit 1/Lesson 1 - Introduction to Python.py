
## Note that to open a python file, simply go on console -> File -> Open

## Two ways to run program
# 1. Run -> Run Module -> OK to save -> get you back to console
# 2. Press F5 (or fn + f5)

# booleans are just another type of integers (1-bit). True = 1, False = 0
# you can actually run programs with integers and booleans combined. Example:

print(False + 293428) # false = 0 so it prints the same value
print(False + False) # false = 0 so it will print 0

# however if u put either booleans alone it will just print True or False

print(True) # this simply prints true
print(False) # this simply prints false

# You can either add or multiply strings, but you can't substract
# Anything can be converted to strings using str(), even booleans

print(str(True)) # This prints True and NOT 1 (it is solo)

# However if booleans aren't alone then it will print integers when you use str

print(str(True + True))
# This prints 2 because booleans aren't alone so considered integers

print(int(True))
print(float(3))
print(int(3.0))

# Note that int() and str() both work with negative numbers

# You can convert strings OR 0 as an int OR 1 as an int to booleans using bool()
