"""
## Draw a flowchart that determines if a number is positive negative or zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

## Draw a flochart that determines if a number is a multiple of 3. If it is
## display "Hello", otherwise display "Bye"

num = int(input("Enter a number: "))
rem = num % 3 # Note that we only do this to draw the flowcharts
if rem == 0:
    print("Hello")
else:
    print("Bye")

## Add all the numbers from 1 to 10, then display the result

acc = 0
num = 1
while num <= 10:
    acc += num
    num += 1
print(acc)

## Draw a flowchart for the following situation: Ask the user to enter a name.
## If the user enters a name, the program will ask for the next name.
## If the user enters “DONE”, the program terminates and the computer
## displays the total number of names entered.
num = 0
name = input("Enter a name:")
while name != "DONE":
    num += 1
    name = input("Enter a name:")
print(num)

## Draw a flochart that addes two numbers together then displays the result to
## the screen

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
result = num1 + num2
print(result)

"""
## Multiply all the odd numbers from 50 to 100, and then display the result.
num = 51
acc = 1
while num < 54:
    acc = acc*num
    num += 2
print(acc)
    
