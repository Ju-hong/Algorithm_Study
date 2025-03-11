import sys

n = int(sys.stdin.readline().strip())

temp = [int(num.strip()) for num in sys.stdin.readlines()]

for num1 in range(n):
    floor = temp[2*num1]     #1층
    number = temp[2*num1+1] #3호
    zero = [_ for _ in range(1, number+1)] 

    for num2 in range(floor): 
        for num3 in range(1, number):
            zero[num3] += zero[num3-1]
    
    print(zero[-1])