# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())

for i in range(n):
    m = input().split()
    if m[0] == 'append':
        d.append(int(m[1]))
    elif m[0] == 'appendleft':
        d.appendleft(int(m[1]))
    elif m[0] == 'clear':
        d.clear()
    elif m[0] == 'appendleft':
        d.appendleft(int(m[1]))
    elif m[0] == 'extend':
        d.extend(int(m[1]))
    elif m[0] == 'extendleft':
        d.extendleft(int(m[1]))
    elif m[0] == 'count':
        d.count()
    elif m[0] == 'pop':
        d.pop()
    elif m[0] == 'popleft':
        d.popleft()
    elif m[0] == 'remove':
        d.remove(int(m[1]))
    elif m[0] == 'reverse':
        d.reverse()
    elif m[0] == 'rotate':
        d.rotate(int(m[1]))

for x in d:
    print(x , end= " ")
