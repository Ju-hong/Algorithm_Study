import sys

n, m = map(int, sys.stdin.readline().split())

d_arr = list(sys.stdin.readline().rstrip() for _ in range(n))
b_arr = list(sys.stdin.readline().rstrip() for _ in range(m))

result = list(set(d_arr) & set(b_arr))

print(len(result))
print('\n'.join(sorted(result)))
        

