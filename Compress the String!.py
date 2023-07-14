# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
groups = []
S = input()
for k, g in groupby(S):
    groups.append((len(list(g)),int(k)))

print(*groups)
