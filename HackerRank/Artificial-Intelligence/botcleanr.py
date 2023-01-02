# https://www.hackerrank.com/challenges/botcleanr

d = []
def trash(board):
  global d,calc
  if d == []:
    r = len(board)
    for y in range(r):
      for x in range(r):
        if board[y][x] == 'd':
          d += [[y,x]]
    calc = 0
    trash(board)
  else:
    return
def nextMove(posr, posc ,board):
  global d
  trash(board)
  if posr==d[0][0] and posc==d[0][1]:
    fn = 'CLEAN'
    d.pop(-1)
  elif posc < d[0][1]:
    fn = 'RIGHT'
  elif posc > d[0][1]:
    fn = 'LEFT'
  elif posr < d[0][0]:
    fn = 'DOWN'
  elif posr > d[0][0]:
    fn = 'UP'
  else:
    pass
  print(fn)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
