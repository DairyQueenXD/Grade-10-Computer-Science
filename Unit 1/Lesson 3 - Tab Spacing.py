## Exercises

print("\"\\\\\"hn\nnh\\\\\"") # this prints "\\"hn (new line) nh\\"
print("")
print("\\\\\"''\"'\\\\'\\'") # this prints \\"''"'\\'\'

# Tab spacing \t

# When you press tab button, the cursor goes to the next positon multiple of 8
# AND NOT space by 8 positions !!!!!!!
print("")
print("012345678901234567890123456789")
print("ab\tHello\tBye\n")
# this prints: ab(position 0-1) Hello (position 8-12) Bye (position 16-18)

print("012345678901234567890123456789")
print("Chowchow\tCS\tClass!\n")
# this prints: chowchow (pos 0-7) CS (pos 16-17) Class! (pos 24-29)

# Note that after chowchow, the tab goes to position 16 because after chowchow,
# The cursor is ALREADY on position 8!

# What is the purpose of using tab spacing?
# To format display into columns, for example to display the following:

# Name  Grade   Mark
# Amy   10      99.2
# Bobby 12      74.2
# Cathy 11      63.3

# We would write the following:
print("Name\tGrade\tMark")
print("Amy\t10\t99.2")
print("Bobby\t12\t74.2")
print("Cathy\t11\t63.3")

# If the name is over 8 characters, we would remove one \t
print("Daniella9\t60.5\n")

# What woould the following display in the console?
print("012345678901234567890123456789")
print("\\\\\"\"\tabc\n\tef\"\t\\")
# This would print: pos 0-3 \\"" pos 8-10 abc
# (New line) pos 8-10 ef"  pos 16 \
