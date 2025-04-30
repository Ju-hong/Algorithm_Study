import sys

n, m = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

result = []

for i in range(n-7):
    for j in range(m-7):

        black_first = 0 
        white_first = 0
        
        for a in range(i, i+8): 
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'W':
                        white_first += 1 # 흰칠 + 1
                    else:
                        black_first += 1
                else:
                    if arr[a][b] != 'W':
                        black_first += 1
                    else:
                        white_first += 1    
    
        result.append(black_first)
        result.append(white_first)

print(min(result))