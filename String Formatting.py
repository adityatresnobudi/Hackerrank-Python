def print_formatted(number):
    # your code goes here
    s = len(str(bin(number)).replace("0b",""))
    for i in range (1, number+1):
        print(f"{str(i).rjust(s,' ')} {oct(i)[2:].rjust(s,' ')} {hex(i)[2:].upper().rjust(s,' ')} {bin(i)[2:].rjust(s,' ')}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
