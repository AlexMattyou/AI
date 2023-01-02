# https://www.hackerrank.com/challenges/saveprincess2/submissions/game/306635195

n = int(input())
p,m = [],[int(x) for x in input().split()]
move = ''
for i in range(n):
  inn = input()
  for j in range(n):
    if inn[j] == 'p':
      p = [i,j]
      break
if m[0] > p[0]:
  m[0] -= 1
  move = 'UP'
elif m[0] < p[0]:
  m[0] += 1
  move = 'DOWN'
elif m[1] > p[1]:
  m[1] -= 1
  move = 'LEFT'
elif m[1] < p[1]:
  m[0] += 1
  move = 'RIGHT'
else:
  pass
print(move)
