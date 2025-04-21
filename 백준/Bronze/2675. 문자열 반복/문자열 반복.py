import sys

k = sys.stdin.readline()

for _ in range(int(k)):
    count, words = sys.stdin.readline().rstrip().split()
    for i in words:
      print(i*int(count), sep='', end = '')
    print('')