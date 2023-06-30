# Enter your code here. Read input from STDIN. Print output to STDOUT
mat_input = input().split()

n, m = int(mat_input[0]), int(mat_input[1])

tgt = 1

for line in range (n+1):
    if line < (n//2):
        print((".|." * tgt).center(m, "-"))
        tgt += 2
    elif line == round(n/2):
        print("WELCOME".center(m, "-"))
    elif line > (n//2) and tgt > 1:
        tgt -= 2
        print((".|." * tgt).center(m, "-"))
