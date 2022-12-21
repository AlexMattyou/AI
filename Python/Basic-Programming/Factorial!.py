# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

x = int(input())
f = 1
for i in range(1,x+1):
    f *= i
print(f)
