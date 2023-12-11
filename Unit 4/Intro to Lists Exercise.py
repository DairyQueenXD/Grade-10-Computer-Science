numList1 = [3,4,5,2,9,3]
print(numList1[0] == numList1[-1])

numList2 = [1,2,3,4,5,6,7,8,9]
counter = 0
for n in numList2:
    if n % 3 == 0:
        counter += 1
print(counter)

numList3 = [1,2,3,4,5,6,7,8,9]
sum = 0
for n in numList3:
    if n % 3 == 0:
        sum += n
print(sum)

numList4 = [1,3,3,2,1]
sum = 0
for n in numList4:
    sum += n
print(sum == 10)

numList5 = [1,2,3,4,5,6]
av = 0
if len(numList5) %2 == 0:
    av = (numList5[int(len(numList5)/2-1)]+numList5[int(len(numList5)/2+1)]) / 2
else:
    av = numList5[int(len(numList5)/2)]
print(av)

charList = ["b","c","e","p","f"]
boo = True
for c in range(len(charList)):
    for i in range(c+1,len(charList)):
        if ord(charList[c]) > ord(charList[i]):
            boo = False
print(boo)

