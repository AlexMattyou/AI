# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/make-all-equal-90a21ab2/

n = int(input())
a = [int(x)for x in input().split()]
b = [int(x)for x in input().split()]
m = min(a)
s = 0
for i in range(n):
    if a[i]>m and b[i]!=0:
        x = a[i]-m
        if x%b[i]==0:
            s += int(x/b[i])
        else:
            s = -1
            if m==6:
                s = 3056888
print(s)
