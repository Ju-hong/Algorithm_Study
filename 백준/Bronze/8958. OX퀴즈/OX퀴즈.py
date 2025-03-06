import sys, re

n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = re.split(r"X+", sys.stdin.readline().strip())
    number = 0
    for word in temp: #00
        count = 0
        for i in word:
            number = number +1 +count
            count += 1
    print(number)