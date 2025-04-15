import sys

arr = sorted(list(map(int, sys.stdin.readlines())))
print(int(sum(arr)/len(arr)), arr[int(len(arr)/2)], sep = '\n')