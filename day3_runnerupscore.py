if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    v=sorted(list(set(arr)))
    v.pop()
    print(v[-1])
