# Rounding down
# Given a float, if we want to ROUND DOWN then just use int()
x = 5.2
y = 5.5
z = 5.9999999
# Rounding down means that we want x y z to be all 5.
x = int(x)
y = int(y)
z = int(z)

print(x)
print(y)
print(z)

# Rounding up
# Given a float, if we want to ROUND UP then just add 1 to the variable and then apply int()
x = 5.2
y = 5.5
z = 5.9999999
# Rounding up means that we want x y z to be all 6.
print(int(x+1))
print(int(y+1))
print(int(z+1))

# Rounding (off)
# Given a float, if we want to ROUND OFF to the nearest integer, add 0.5 and apply int()
x = 5.2
y = 5.5
z = 5.9999999
# We want x to be 5, y to be 6, z to be 6
print(int(x+0.5))
print(int(y+0.5))
print(int(z+0.5))

# Rounding to the nearest x decimal places
# Example: 97.5678 to the nearest 2 decimal places
n = 97.5678
n *= 100
print(int(n+0.5)/100)

