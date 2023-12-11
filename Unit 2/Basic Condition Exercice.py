print("\n----------------------- Part 1 ----------------------")
item = 7
num  =11
print((2 * item) == num)
print((2 * item - 1) < num)
print((item <= 7) and (num <= 7))
print((item <= 7) or (num <= 7))
print((item > 0) and (item <= 10))
print((item <= 11) or (num <= 11))
print((item > 25) or (item < 50) or (num < 50))
print((item != 5) and (item != 6))
print((item < 5) or (item > 6))
print(not (not (not (item != 7))))

print("----------------------- Part 2 ----------------------")
Cat = True
Rat = False
print((Cat and Rat) or Rat)		
print(Cat or (Rat and (not Cat)))
print(not Rat and not Rat)

print("----------------------- Part 3 ----------------------")
Grade = "C"
RealValue = 3.97	
IntegerValue = 5

print(RealValue <= 5)
print(IntegerValue < RealValue)   
print(Grade <= "D")
print(29 / 5 == IntegerValue)

print("----------------------- Part 4 ----------------------")
# Test data:  grapes, bananas | apples, oranges | KIWI, kiwi

fruit1 = input ("Enter the first fruit: ")
fruit2 = input ("Enter the second fruit: ")
if fruit1 < fruit2:
    print (fruit1, "is before", fruit2, "alphabetically.")
else:
    print (fruit2, "is before", fruit1, "alphabetically.")

print("----------------------- Part 5 ----------------------")
# Test data:  6, 4 | 5, 8 | 0, 2 | 17, 0

number1 = int (input ("Enter the first number: "))
number2 = int (input ("Enter the second number: "))
if number2 == 0:
    print ("The quotient is undefined.")
else:
    quotient = (number1 * 1.0) / number2
    print (number1, "/", number2, "=", quotient)

print("----------------------- Part 6 ----------------------")

name = input ("Enter your name: ")
gender = input("Enter your gender - f or m: ")
time = float(input("Enter your time for the 100 meters: "))

if (gender == "f" or gender == "F") and (time < 10.87):
    print (name, ", you're lying; no one can run faster than world record holder.")
elif (gender == "f" or gender == "F") and (time <= 11.2):
    print (name, ", you are close behind the world record holder.")
elif (gender == "f" or gender == "F") and (time <= 11.5):
    print (name, ", you have potential.")
elif (gender == "f" or gender == "F") and (time <= 13):
    print (name, ", keep working and you shall improve.")
elif (gender == "f" or gender == "F"):
    print (name, ", Give up - you are too slow.")
else:
    print (name, ", this is for females only.  Go to the next machine for males.")

print("----------------------- Part 7 ----------------------")
city = input("What is the capital of Ontario? ")
if city == "Toronto":
	print("correct")
else:
    print("incorrect")

print("----------------------- Part 8 ----------------------")
cost = float(input("How much did your meal cost? "))
if cost > 4:
    cost = cost*1.07
    print(cost)
else:
    print(cost)


print("----------------------- Part 9 ----------------------")
num1 = float(input("Enter in the first number: "))
num2 = float(input("Enter in the second number: "))
sum = float(input("Enter in the sum: "))
if num1 + num2 == sum:
    print("correct")
else:
    print(num1+num2)

month = int(input("Enter a number: "))

if month == 12 or 1 <= month <= 3:
    print("Winter")
elif month == 4 or month == 5:
    print("Spring")
elif 6<= month <= 8:
    print("Summer")
else:
    print("Autumn")