def split_and_join(line):
    # write your code here
    spaced = line.split(" ")
    dashed = "-".join(spaced)
    return dashed

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
