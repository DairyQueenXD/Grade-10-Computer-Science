"""
Program 1: This program asks the user for their name and their favourite ice
cream flavour. Then, it prints both responses in one line/sentence

"""
# Asking for the user's name
name = input("What is your name?: ")
# Asking for the user's favourite ice cream flavour
ice_cream_flavour = input("What is your favourite ice cream flavour?: ")
# Printing both responses in one line
print("Your name is " + name + " and your favourite ice cream flavour is " + ice_cream_flavour + ".\n")

"""
Program 2: This program asks the user for their first name, last name at age one at a time.
Then, it prints a sentence containing these three information in the following format:
Hello lastname, firstname. You are age years old!

"""
# Asking for the user's first name
first_name = input("What is your first name?: ")
# Asking for the user's last name
last_name = input("What is your last name?: ")
# Asking for the user's age
age = input("How old are you?: ")
# Printing the collected info in one sentence
print("Hello " + last_name + ", " + first_name + ". You are " + age + " years old!\n")

"""
Program 3: This program asks the user for a street number, a street, a city, a province and
a postal code. Then, it displays the entire adddress all on one line, with commas between
all the items except for street number and street.

"""
# Asking for a street number
street_number = input("Enter a street number: ")
# Asking for a street
street = input("Enter a street: ")
# Asking for a city
city = input("Enter a city: ")
# Asking for a province
province = input("Enter a province: ")
# Asking for a postal code
postal_code = input("Enter a postal code: ")
# Printing the final statement
print(street_number + " " + street + ", " + city + ", " + province + ", " + postal_code + "\n")

"""
Program 4: This program asks the user to input 2 integers, and displays the sum, difference,
product and quotient.

"""
# Asking for the first integer
int1 = int(input("Enter the first number: "))
# Asking for the second integer
int2 = int(input("Enter the second number: "))
# Creating a variable that stores the sum of the two numbers
sum_of = int1 + int2
# Creating a variable that stores the difference of the two numbers
difference = int1 - int2
# Creating a variable that stores the product of the two numbers
product = int1 * int2
# Creating a variable that stores the quotient of the two numbers
quotient = int1 / int2
# Printing the addition statement
print(str(int1) + " + " + str(int2) + " = " + str(sum_of))
# Printing the substraction statement
print(str(int1) + " - " + str(int2) + " = " + str(difference))
# Printing the multiplication statement
print(str(int1) + " x " + str(int2) + " = " + str(product))
# Printing the division statement
print(str(int1) + " / " + str(int2) + " = " + str(quotient) + "\n")

"""
Program 5: This program asks the user to enter a length in cm. Then, it displays the
corresponding length in inch, rounding the answer to 2 decimal places.

"""
# Asking for the length in centimeter
length_cm = input("Enter length in cm: ")
# Converting the length to inch, and storing the new number in a variable
length_inch = int((float(length_cm)/2.54)*100)/100
# Printing the conversion statement
print(length_cm + " cm = " + str(length_inch) + " inch\n")

"""
Program 6: This program asks the user for a subject in school, the total mark on a test in
that subject, and their test mark. Then, it displays the test mark as a percentage rounded
down to 1 decimal place.

"""
# Asking for the subject
subject = input("Subject: ")
# Asking for the total mark on a test
total_mark = float(input("Total Mark: "))
# Asking for the test mark
test_mark = float(input("Test Mark: "))
# Storing the percentage in a variable
percentage = int(test_mark / total_mark * 1000)/10
# Printing the final statement with the percentage
print("You got " + str(percentage) + "%\n")

"""
Program 7: This program asks the user to input the starting time and finishing time of an
automobile day trip as well as the distance in km traveled. It then displays the average
speed in km/h, rounded down to 2 decimals.

"""
# Asking for the starting hour
start_hour = int(input("Starting Hour : "))
# Asking for the starting minute
start_min = int(input("Starting Min  : "))
# Asking for the ending hour
end_hour = int(input("Ending Hour   : "))
# Asking for the ending minute
end_min = int(input("Ending Min    : "))
# Asking for the distance
distance = float(input("Distance      : "))
# Calculating the time of the trip in minutes
minutes = (end_hour*60 + end_min) - (start_hour*60 + start_min)
# Printing the final statement
print("\nAverage Speed : " + str(int(distance / minutes * 60 * 100)/100) + " km/h")


