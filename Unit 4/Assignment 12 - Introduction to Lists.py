start_list = []
new_list = []
while True:
    counter_two = 0
    counter_three = 0
    print("List Menu\n\nCurrent list: "+str(start_list)+"\n")
    print("1 - Create New String List\n2 - Count Number of Vowels from List")
    print("3 - Count Number of Upper Case Letters from List")
    print("4 - Display the String List with all Vowels Removed")
    print("5 - Exit List Menu Program\n")
    option = int(input("Enter Option Number: "))
    if option == 5:
        break
    elif option == 1:
        start_list = []
        num = int(input("\nNumber of strings you'd like to enter into the list: "))
        for i in range(num):
            start_list.append(input("String #" + str(i+1) +": "))
        print("---------------------------------------------------------------\n")
        #print(start_list[0][len(start_list[0])-1])
    elif option == 2:
        for i in range(num):
            for x in range(len(start_list[i])):
                if start_list[i][x].lower() == "a" or start_list[i][x].lower() == "e" or start_list[i][x].lower() == "i" or start_list[i][x].lower() == "o" or start_list[i][x].lower() == "u":
                    counter_two += 1
        print("\nThere are " + str(counter_two) + " vowels")
        print("---------------------------------------------------------------\n")
    elif option == 3:
        for c in range(num):
            for d in range(len(start_list[c])):
                if 65 <= ord(start_list[c][d]) <= 90: 
                    counter_three += 1
        print("\nThere are " + str(counter_three) + " upper case letters")
        print("---------------------------------------------------------------\n")
    elif option == 4:
        new_list = []
        for i in range(num):
            new_list.append(start_list[i])
        for a in range(num):
            for b in range(len(new_list[a])):
                if new_list[a][b].lower() == "a" or new_list[a][b].lower() == "e" or new_list[a][b].lower() == "i" or new_list[a][b].lower() == "o" or new_list[a][b].lower() == "u":
                    new_list[a] = new_list[a][:b] + str(" ") + new_list[a][b+1:]
        for h in range(num):
            for z in range(len(new_list[h])):
                new_list[h] = new_list[h].replace(" ","")
        print("\nString List with all Vowels Removed " + str(new_list))
        print("---------------------------------------------------------------\n")
    
