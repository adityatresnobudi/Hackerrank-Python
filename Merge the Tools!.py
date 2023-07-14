def merge_the_tools(string, k):
    # your code goes here
    dic = {}
    for i in range (1,len(string)+1) :
        dic.update({string[i-1]:'0'})
        if i % k == 0 :
            print("".join(dic.keys()))
            dic = {}
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
