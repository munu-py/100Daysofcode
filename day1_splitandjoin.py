def split_and_join(line):
    l=line.split()
    l1=""
    l1="-".join(l)
    return l1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)