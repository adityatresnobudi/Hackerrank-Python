# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

totalPrice = 0

n = int(input())
sizeList = list(map(int, input().split()))
sizeKey = list(Counter(sizeList).keys())
sizeVal = list(Counter(sizeList).values())
buy = int(input())

for i in range(buy):
    size, price = map(int, input().split())
    if size in sizeKey:
        if sizeVal[sizeKey.index(size)] != 0:
            sizeVal[sizeKey.index(size)] -= 1
            totalPrice += price
        else:
            pass
    else:
        pass
print(totalPrice)
