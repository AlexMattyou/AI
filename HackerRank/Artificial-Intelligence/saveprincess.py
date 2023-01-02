# https://www.hackerrank.com/challenges/saveprincess/submissions/game/306595421

n = int(input())
m,p = [],[]
for i in range(n):
  inn = input()
  for j in range(n):
    if inn[j] == 'm':
      m = [i,j]
    elif inn[j] == 'p':
      p = [i,j]
for x in range(min([m[0],p[0]]),max([m[0],p[0]])):
  if m[0] > p[0]:
    m[0] -= 1
    print('UP')
  elif m[0] < p[0]:
    m[0] += 1
    print('DOWN')
  else:
    continue
for y in range(min([m[1],p[1]]),max([m[1],p[1]])):
  if m[1] > p[1]:
    m[1] -= 1
    print('LEFT')
  elif m[1] < p[1]:
    m[0] += 1
    print('RIGHT')
  else:
    continue
