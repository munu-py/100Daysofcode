def mutate_string(string, position, character):
    list1=list(s)
    list1[int(i)]=c
    s1="".join(list1)
    return s1



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)