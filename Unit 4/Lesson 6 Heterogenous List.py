abcd = [1,5,4.35,2,16,"HELLO",4]
counter = 0
for i in range(len(abcd)):
    if type(abcd[i]) == int:
        counter += 1
print(counter)

efgh = [3,True,"abc",1.5,3.3,"negative",1.2,16]
s = 0
for i in range(len(efgh)):
    if type(efgh[i]) == float:
        s += efgh[i]
print(s)

ijkl = [4,5,True,"abc",3,False,"123",4.2,1]
newList1 = []
for i in ijkl:
    if type(i) == int:
        newList1.append(i)
print(newList1)

mop = [False,"Hello","comp","sci",123,"class","!",3.1415]
newList2 = []
for i in mop:
    if type(i) == str and len(i) >= 5:
        newList2.append(i)
print(newList2)