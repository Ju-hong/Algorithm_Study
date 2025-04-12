import sys

count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def finding(num):
  if num != 1:
    for i in range(2, int(num**0.5)+1):
      if num%i == 0:
        return False
    return True
      
for num in arr:
  if not finding(num):
    count -= 1

print(count)