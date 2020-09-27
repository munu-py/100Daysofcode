def count_substring(string, sub_string):
    l=len(string)
    count=0
    for i in range(l):
        temp=""
        for j in range(i,l):
            temp+=string[j]
            if(temp==sub_string):
                count+=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)