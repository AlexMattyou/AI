# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

i = input().strip().lower()
a,b = 0,0
for x in i:
    if x=='z':
        a += 1
    else:
        b += 1
if b/a == 2:
    print('Yes')
else:
    print('No')
