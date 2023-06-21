if __name__ == '__main__':
    n = int(input())
    num = 0
    for i in range (n):
        if ((i+1) / 10) < 1:
            num = num * 10 + (i + 1)
        elif ((i+1) / 10) < 10 and ((i+1) / 10) >= 1:
            num = num * 100 + (i + 1)
        else:
            num = num * 1000 + (i + 1)
    print(num)
