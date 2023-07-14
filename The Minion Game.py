def minion_game(string):
    # your code goes here
    vowel= "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(len(string)) :
        if string[i] in vowel:
            score = len(string) - i
            kevin += score
        else :
            score = len(string) - i
            stuart += score
            
    if stuart > kevin :
        print("Stuart {}".format(stuart))
    elif kevin > stuart :
        print("Kevin {}".format(kevin))
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
