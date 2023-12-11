## Number 1
length = 0
for i in range(10):
    string = input("Enter a word: ")
    if string == "wow":
        break
    print(len(string))
    length += len(string)
print(length/10)

## Number 2
while True:
    string = input("Enter a word: ")
    if string == "wow":
        break
    if len(string) %2 == 0:
        print("The middle letters are " + string[int(len(string)/2-1):int(len(string)/2+1)])
    else:
        print("The middle letter is " + string[int(len(string)//2)])

## Number 3
while True:
    output = ""
    string = input("Enter a word: ")
    if string == "wow":
        break
    if len(string)%2 == 0:
        for i in range(1,len(string),2):
            output += string[i]
        print("Output:",output)
    else:
        for i in range(0,len(string),2):
            output += string[i]
        print("Output:",output)

## Number 4
while True:
    new = ""
    string = input("Enter a word: ")
    if string == "wow":
        break
    for i in range(len(string)-1):
        print(string[i],end="-")
    print(string[len(string)-1])

## Number 5
while True:
    string = input("Enter a word: ")
    if string == "wow":
        break
    if len(string) <= 1:
        print("Output:",string,"is invalid.")
    else:
        print("Output:",string[0]+string[-1]+", "+string[1:-1])

## Number 6
while True:
    new = ""
    string = input("Enter a word: ")
    if string == "wow":
        break
    for i in range(len(string)):
        a = i*-1-1
        new += string[a]
    print("The reverse word is",new)
    
        
        
