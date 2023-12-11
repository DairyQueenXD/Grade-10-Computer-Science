
while True:
    counter = 0
    print("String Menu\n\n1 - Count pattern\n2 - Eliminate pattern\n3 - Substitute pattern\n4 - Exit String Menu Program\n")
    num = int(input("Enter Option Number: "))

    if num == 1 or num == 2:
        string = input("Enter String: ")
        chr = input("Enter Character: ")
    elif num == 3:
        string = input("Enter String: ")
        c1 = input("Enter Character 1: ")
        c2 = input("Enter Character 2: ")
    elif num == 4:
        break
    if num == 1:
        test = string
        for i in range(int(len(string) / len(chr))):
            if test.find(chr) != -1:
                a = test.find(chr)
                test = test[a+1:]
                counter += 1
        print(chr + " appeared " + str(counter) + " times in " +  string + "\n")
    elif num == 2:
        test2 = string
        for i in range(int(len(string))):
            if test2.find(chr) != -1:
                a = test2.find(chr)
                test2 = test2[:a] + test2[a+len(chr):]
        print("Removing " + chr + " from " + string + " yields " + test2 + "\n")
    elif num == 3:
        test3 = string
        for i in range(int(len(string))):
            if test3.find(c1) != -1:
                a = test3.find(c1)
                test3 = test3[:a] + c2 + test3[a+len(c1):]
        print("Replacing " + c1 + " with " + c2 + " from " + string + " yields " + test3)

    
