import sys

n, m = map(int, sys.stdin.readline().split())

pocket = {}

for i in range(1, n+1):
  a = sys.stdin.readline().rstrip()
  pocket[i] = a
  pocket[a] = i

question = list(sys.stdin.readline().rstrip() for _ in range(m))
  
for q in question:
    if q[0].isalpha():
       print(pocket[q])
    else:
       print(pocket[int(q)])