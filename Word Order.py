# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
count_set = Counter()
for i in range(n):
    string = input().split("\n")
    count_set.update(string)
print(len(list(count_set.keys())))
for i in count_set.values():
    print(i, end= " ")
