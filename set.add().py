# Enter your code here. Read input from STDIN. Print output to STDOUT
stamps = set()
n = int(input())
for i in range(n):
    country = input()
    stamps.add(country)
print(len(list(stamps)))
