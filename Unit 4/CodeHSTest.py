word = input("Enter a word: ")
def get_index(index):
    if index == -1:
        quit()
    while index < 0 or index > len(word)-1:
        print("Invalid index")
        index = int(input("Enter an index (-1 to quit): ")) 
def get_letter(letter):
    while len(letter) != 1 or letter.lower() != letter:
        if len(letter) != -1:
            print("Must be exactly one character!")
        elif letter.lower() != letter:
            print("Character must be a lowercase letter!")
        letter = input("Enter a letter: ")
while True:
    index = int(input("Enter an index (-1 to quit): "))
    letter = input("Enter a letter: ")
    get_index(index)
    get_letter(letter)
    a = [word]
    print(a)
    print(a[0][index])
    a[0][index] = letter
    print(str(a))
        
