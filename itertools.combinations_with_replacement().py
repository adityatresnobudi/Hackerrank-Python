# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr
s, k = input().split()
for i in cwr(sorted(s), int(k)):
    print("".join(i))
