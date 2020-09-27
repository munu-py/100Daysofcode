def minion_game(string):
    count1 = 0
    count2 = 0
    if(len(string)<=100000 and string.isupper()):
        list1 = ['A', 'E', 'I', 'O', 'U']

        for i in range(0, len(string)):
            if (string[i] in list1):
                count1 += len(string) - i
            else:
                count2 += len(string) - i
    else:
        print("wrong input")
    if(count1>count2):
        print("Kevin", count1)
    elif(count2>count1):
        print("Stuart", count2)
    else:
        print("Draw")





if __name__ == '__main__':
    s = input()
    minion_game(s)