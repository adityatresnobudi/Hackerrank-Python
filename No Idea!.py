# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0

nm = input().split()
n = list(input().split())
aNum = set(input().split())
bNum = set(input().split())

for n in n:
    if n in aNum:
        happiness += 1

    elif n in bNum:
        happiness -= 1

    else:
        continue

print(happiness)
