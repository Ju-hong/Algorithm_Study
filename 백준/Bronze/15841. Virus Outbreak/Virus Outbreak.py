import sys

arr = list(map(int, sys.stdin.readlines()))
fibo_list = [0, 1, 1]

for _ in range(2, max(arr)):
    fibo_list.append(fibo_list[-2]+fibo_list[-1])

for j in arr[:-1]:
    print(f"Hour {j}: {fibo_list[j]} cow(s) affected")