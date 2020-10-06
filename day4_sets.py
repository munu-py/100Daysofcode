def average(array):
    # your code goes here
    s1=set(arr)
    l=len(s1)
    sum=0
    for x in s1:
        sum+=x
    avg=sum/l
    return avg

#------------------------------
n,m=input().split()
arr=input().split()
set1=set(input().split())
set2=set(input().split())
h=0
for i in arr:
    if i in set1:
        h+=1
    if i in set2:
        h-=1
    else:
        continue
print(h)

#--------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
list1= set(map(int,input().split()))
m=int(input())
list2=set(map(int,input().split()))
z=list(list1.symmetric_difference(list2))
z.sort()
for i in z:
    print(i)
#----------------------------------
n=int(input())
set1=set()
for i in range(n):
    set1.add(input())
print(len(set1))
#----------------------------------
n=int(input())
l=input().split()
set1=set()
set2=set()
for i in l:
    if i not in set1:
        set1.add(i)
    else:
        set2.add(i)
z=set1.difference(set2)
print(z.pop())
