## Number 2

number = int(input("Enter an integer: "))
while number != 0:
    rem = number % 2
    if rem == 0:
        print("even")
    else:
        print("odd")
    number = int(input("Enter an integer: "))

## Number 4

sentence = input("Enter a sentence: ")
num = int(input("Enter a number: "))
acc = 0
while acc != num:
    print(sentence)
    acc += 1
    