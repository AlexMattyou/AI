# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

ans = 'Yes'
N = int(input())
data = [int(x) for x in input().split()]
s = ''
for i in data:
    i = str(i)[-1]
    s += i
s = int(s)
if s%10!=0:
    ans = 'No'
print(ans)
