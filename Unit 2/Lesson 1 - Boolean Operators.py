# When comparing strings, its basically just alphabet
print("bf" > "gf")
print("zebra" > "dog")
print("Markville" > "Unionville")
print("BMW" > "Toyota")
print("boy" > "girl")
print("noodles" > "rice")
print("oragne" > "oracle")
print("n" > "c")

# What if there is a space
# the space is compared, and is smaller than any letter and symbols
print("I love CS" < "Igloo") # This prints true because space < g

# And numbers?
# numbers are smaller than any letters
print("se7en" < "seven")

# What about capital letters?
# Capital letters are smaller than other letters
print("Zebra" < "student")

# Summary
# Space < Numbers < Upper case letters < Lower case letters
# In lower case letters, a < z , x < y, etc.