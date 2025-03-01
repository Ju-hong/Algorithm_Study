import sys

def number(a):
    if a % 15 ==0 :
        return "FizzBuzz"
    elif a%5 == 0:
        return "Buzz"
    elif a%3 == 0:
        return "Fizz"
    else:
        return a

temp = [sys.stdin.readline().strip() for _ in range(3)]

for i in temp:
    try:
        int(i)
        x = (3 - temp.index(i)) + int(i)
        print(number(x))
        break
    except:
        pass