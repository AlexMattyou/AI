# https://www.hackerrank.com/challenges/botclean/submissions/game/307773805

d = []
calc = 1
def trash(board):
  global d,calc
  if calc:
    r = len(board)
    for y in range(r):
      for x in range(r):
        if board[y][x] == 'd':
          d += [[y,x]]
    calc = 0
    trash(board)
  else:
    return
def next_move(posr, posc ,board):
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
