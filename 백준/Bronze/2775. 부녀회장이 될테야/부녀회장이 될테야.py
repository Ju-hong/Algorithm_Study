import sys

n = int(sys.stdin.readline().strip())

temp = [int(num.strip()) for num in sys.stdin.readlines()]

for num1 in range(n):
    floor = temp[2*num1]     #1층
    number = temp[2*num1+1] #3호


    zero = [k for k in range(1, number+1)] #0번 위치

    for num2 in range(floor): # 1
        new = []

        for num3 in range(number): # 3
            new.append(sum(zero[:num3+1]))

        zero = new
    print(zero[-1])