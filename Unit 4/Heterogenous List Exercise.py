someList = ["I",3.1415,"love",True,"CS",100]
counter = 0
for i in someList:
    if type(i) == str:
        counter += 1
print(counter)

heteList = [False,True,123,True,4.96]
counter = 0
for i in heteList:
    if type(i) == bool and type(i) == True:
        counter += 1
print(counter)

aList = ["mister",12,False,3,"Chow"]
newList = []
for i in aList:
    if type(i) == str:
        newList.append(i)
print(newList)

randList = [False,15,"two",4,21,"five",6,11]
newList2 = []
for i in randList:
    if type(i) == int and (i%3==0 or i%5 == 0):
        newList2.append(i)
print(newList2)