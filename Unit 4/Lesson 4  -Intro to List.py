names = ["Dora", "Matthew","Sarina","Nicholas","Dequan","Tinsly"]
names2 = ["Ivan","Lori","Arun"]
"""
To add new elements into list, 
1) .append function
2) Adding another list
"""
names.append("Zifan")
names += ["Thomas"]
print(names)
## We can also add two lists together
names3 = names + names2

"""
List does NOT need to be homogenous
-> homogenous = all elements have to belong in same type
A list can contain items of different data types
"""
student1 = ["Dora", 87]
student2 = ["Tinsly", 93.2]
student3 = ["Thomas", 77]

# .remove function
# Note that .remove only removes the FIRST occurence
fruits = ["apple","pear","apple","orange","watermelon","strawberries"]
fruits.remove("watermelon")
print(fruits)

## Indexing
print(fruits[2])
print(fruits[3][1])

fruits[0] = "blueberries"
print(fruits[0])
print(fruits)

## Length
print(len(fruits))