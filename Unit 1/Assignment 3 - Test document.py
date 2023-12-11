# Asking for the subject
subject = input("Subject: ")
# Asking for the total mark on a test
total_mark = float(input("Total Mark: "))
# Asking for the test mark
test_mark = float(input("Test Mark: "))
# Storing the percentage in a variable
percentage = int(test_mark / total_mark * 1000)/10
# Printing the final statement with the percentage
print("You got " + str(percentage) + "%")
