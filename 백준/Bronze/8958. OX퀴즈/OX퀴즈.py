import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = sys.stdin.readline().strip().split("X")
    number = 0
    for word in temp: #00
        count = 0
        for i in word:
            number = number +1 +count
            count += 1
    print(number)