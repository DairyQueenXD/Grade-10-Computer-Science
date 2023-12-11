
# Exercice 1
x = int(input("Enter a number: "))
if x < 0:
    print("NEGATIVE")
elif x == 0:
    print("ZERO")
elif x % 2 == 0:
    print("EVEN")
else:
    print("ODD")

# Exercice 2

from random import randint
rand_num = randint(1,5)
guess = int(input("Enter a guess: "))
if guess == rand_num:
    print("Correct")
elif guess > rand_num:
    print("Too high")
else:
    print("Too low")

# Exercice 3

weight = float(input("Enter your weight: "))
dose = 0
if weight < 16:
    dose = weight*0.6
    print(int(dose*100+0.5)/100)
elif 16 <= weight < 25:
    dose = weight*0.75
    print(int(dose*100+0.5)/100)
elif 25 <= weight < 40:
    dose = weight*0.83
    print(int(dose*100+0.5)/100)
elif 40 <= weight < 65:
    dose = weight*1.2
    print(int(dose*100+0.5)/100)
else:
    dose = weight*1.3
    print(int(dose*100+0.5)/100)

# Exercise 4

side1 = int(input("Enter side 1: "))
side2  =int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
largest = 0
sum_smallest = 0
if side1 > side2:
    if side1 > side3:
        largest = side1
        sum_smallest = side2 + side3
    else:
        largest = side3
        sum_smallest = side1 + side2
elif side2 > side3:
    largest = side2
    sum_smallest = side1 + side3
else:
    largest = side3
    sum_smallest = side1 + side2

if sum_smallest > largest:
    print("Can be a triangle")
else:
    print("Cannot be a triangle")
