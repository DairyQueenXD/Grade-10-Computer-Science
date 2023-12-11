"""
We use an accumulator in games:
- highscore
- tie-breaker
- timer

"""

## Using a while loop, display:
# 8
# 14
# 20
# ...
# 146
x = 8
while x <= 146:
    print(x)
    x += 6

## Using a while loop, display the answer of:
# 8 + 14 + 20 + ... + 146
print("----------------------------------------")
x = 8
acc1 = 0
while x <= 146:
    acc1 = acc1 + x
    x += 6
print(acc1)

## Using a for loop, display the answer of:
## 6 + 10 + 14 + 18 + ... + 458

acc2 = 0
for i in range(6, 462, 4):
    acc2 += i
print(acc2)

## Using a for loop, display answer of 
## 97 + 83 + 69 + ... + -351
acc3 = 0
for i in range(97, -352, -14):
    acc3 += i
print(acc3)

## Using a while loop, display the answer of
## 3 + 6 + 12 + ... + 25165824
acc4 = 0
y = 3
while y <= 25165824:
    acc4 += y
    y *= 2
print(acc4)

## Using while loop, display answer of 
## 2 - 6 + 18 - 54 + ... + 9565938
acc5 = 0
z = 2
while z != 9565938*-3:
    acc5 += z
    z *= -3
print(acc5)