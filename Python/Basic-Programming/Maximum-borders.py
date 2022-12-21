no = int(input())
for n in range(no):
    i,t = [int(x) for x in input().strip().split()],0
    for x in range(i[0]):
        c = input().count('#')
        if t<c:
            t = c
    print(t)
