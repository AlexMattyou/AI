# https://www.hackerrank.com/challenges/python-lists
N = int(input())
a = []
for l in range(N):
    i = input().split()
    f = i.pop(0).strip().lower()
    i = [int(x) for x in i]
    if f == 'insert':
        a.insert(i[0],i[1])
    elif f == 'print':
        print(a)
    elif f == 'remove':
        a.remove(i[0])
    elif f == 'append':
        a.append(i[0])
    elif f == 'sort':
        a.sort()
    elif f == 'pop':
        a.pop()
    else:
        a.reverse()
