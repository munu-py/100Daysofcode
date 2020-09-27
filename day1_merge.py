def merge_the_tools(string, k):
    # your code goes here
    if(len(string)<=10000 and k<=len(string) and len(string)%k==0):
        for i in range(0,len(string),k):
            newstr=string[i:i+k]
            new=""
            for i in newstr:
                if i not in new:
                    new+=i
            print(new)




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)