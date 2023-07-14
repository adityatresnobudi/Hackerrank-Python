# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, k  = input().split()
s_sorted = "".join(sorted(s))
k = int(k) 

for i in range(1,k+1):
    for combination in list(combinations(s_sorted, i)):
        print("".join(combination))
