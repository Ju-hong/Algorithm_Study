import sys, math

L, A, B, C, D = map(int, sys.stdin.readlines())

max_i =  L - max(math.ceil(A/C), math.ceil(B/D))

if max_i > 0 :
  print(max_i)
else:
  print(0)

