if __name__ == '__main__':
    arr = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        scores.append(score)
    sorted_arr = sorted(arr)
    secondLowest = sorted(set(scores))[1]
    for i in range (len(sorted_arr)):
        if sorted_arr[i][1] == secondLowest:
            print(sorted_arr[i][0])
