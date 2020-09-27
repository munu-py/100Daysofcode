if __name__ == '__main__':
    s = "QA2"
    list1=[]
    lis2=[]
    list3=[]
    list4=[]
    list5=[]
    for i in s:
        list1.append(i.isalnum())
    print(any(list1))
    for j in s:
        lis2.append(j.isalpha())
    print(any(lis2))
    for i in s:
        list3.append(i.isdigit())
    print(any(list3))
    for j in s:
        list4.append(j.islower())
    print(any(list4))
    for i in s:
        list5.append(i.isupper())
    print(any(list5))





