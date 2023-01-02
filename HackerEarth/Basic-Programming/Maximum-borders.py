# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/maximum-border-9767e14c/

no = int(input())
for n in range(no):
    i,t = [int(x) for x in input().strip().split()],0
    for x in range(i[0]):
        c = input().count('#')
        if t<c:
            t = c
    print(t)
