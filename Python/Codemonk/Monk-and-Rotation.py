# https://www.hackerearth.com/practice/codemonk/

for c in range(int(input())):
    i = [int(x) for x in input().split()]
    v = [int(x) for x in input().split()]
    g = i[1]%i[0]
    v = v[-g:]+v[:-g]
    [print(p,end=' ')for p in v]
    print()
