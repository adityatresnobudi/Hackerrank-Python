# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))

c = sorted(a.union(b) - a.intersection(b))

for i in c:
    print(i)
