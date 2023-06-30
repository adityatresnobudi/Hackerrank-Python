def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"[:size]
    width = "-".join([i for i in alphabet[::-1]] + [i for i in alphabet[1:]])
    rangoli = []
    for i in range(1, size+1):
        letters = [i for i in alphabet[-i:]]
        if len(letters) == 1:
            rangoli.append(letters[0].center(len(width), "-"))
        else:
            rangoli.append("-".join(letters[::-1] + letters[1:]).center(len(width), "-"))
    print("\n".join(rangoli + rangoli[::-1][1:]))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
