# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
n = int(input())
arr = input().split(' ')
arr = [int(x) for x in arr]
arr = [x for x in arr if x < max(arr)]
print(max(arr))
