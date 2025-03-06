from collections import deque

n, m = map(int, input().split()) # 7 3

temp = deque([i for i in range(1, n+1)]) # 1~7
final = []

while temp:
    temp.rotate(-m+1)
    final.append(temp.popleft())

print(f"<{", ".join(map(str, final))}>")   