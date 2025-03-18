import sys

def fibo(n):
    arr = [0, 1, 1]

    if n == 0:
        return 1, arr[n]

    elif n == 1:
        return 0, arr[n]   
    
    else:
        for _ in range(3, n+1):
            arr[0], arr[1], arr[2] = arr[1], arr[2], arr[1]+arr[2]
    
    return arr[1], arr[2]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    print(' '.join(map(str, fibo(num))))
