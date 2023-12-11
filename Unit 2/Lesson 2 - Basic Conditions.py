# Test question will look like this
x = -4.5
y = 3
if x > -y:
    print("A")
else:
    print("B")
    print("C")
print("D", end="***")
if x**2 > (-y)**2:
    print("E", end="\t\\\n")
if x/y == -y/2:
    print("F", end="\\\t\\")
if x**0 != y**0:
    print("G", end="\n\\")
else:
    print("H", end="\n**")
    
"""
This would print
B
C
D***E   \
F\      \H
**

"""