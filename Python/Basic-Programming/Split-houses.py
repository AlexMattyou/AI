# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/

n = int(input())
d = input()
a = ''
c = 'YES'
if d.count('HH')>0:
    c = 'NO'
else:
    for i in d:
        if i=='.':
            a+='B'
        else:
            a+='H'
print(c)
print(a)
