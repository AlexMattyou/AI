# https://www.hackerearth.com/submission/78815535/

for inputs in range(int(input())):
    one,two = [],[]
    g,p = map(int,input().split())
    n = int(input())
    for b in range(n):
        i,j = map(int,input().split())
        one.append(i)
        two.append(j)
    sum1,sum2 = sum(one),sum(two)
    print(min((sum1 * g + sum2 * p),(sum1 * p + sum2 * g)))
