total = 0
for i in range (-3, 5, 3):
    total = total + i
    print (i, total)

print("")

howmany = 10
sum = 0
for x in range (howmany, -2, -3):
    sum = sum + x
    print (x, sum)
print (sum / x)

print("")

k = 10
for i in range (2, 20, 5):
    if i >= 17:
       break
    k = k + 2
    print ((k * 1.0) / 2)

print("")

count = 0
for j in range (1, 15, 3): 
    count = count + 5
    print (j, count * 2)
    if count == 20:
       break

print("")

for i in range (1, 4):
    for j in range (1, 6, 2):
      print (i, j)
