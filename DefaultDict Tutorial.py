# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = list(map(int, input().split()))

dictionary = defaultdict(list)

for i in range(n):
    dictionary[input()].append(i+1)

for i in range(m):
    print(" ".join(map(str, dictionary[input()])) or -1)
