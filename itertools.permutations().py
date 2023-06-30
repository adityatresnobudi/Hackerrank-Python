# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def perm(s, size):
    list_perm = ["".join(i) for i in permutations(s,size)]
    
    return "\n".join(sorted(list_perm))


user = input().split(" ")
s, size = user[0], int(user[1])
print(perm(s,size))
