# Enter your code here. Read input from STDIN. Print output to STDOUT\
from collections import OrderedDict

itemNum = int(input())
itemDict = OrderedDict()
for i in range(itemNum):
    itemSales = input().split()
    item, net = " ".join(itemSales[:-1]), int(itemSales[-1])
    
    if item in itemDict:
        itemDict[item] += net
    else:
        itemDict[item] = net

print("\n".join([f"{item} {net}" for item, net in itemDict.items()]))
