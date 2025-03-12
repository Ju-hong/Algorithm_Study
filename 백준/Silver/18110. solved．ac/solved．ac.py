import sys

def rounding(n):
    if n - int(n) < 0.5:
        return int(n)
    else:
        return int(n) + 1

length = int(sys.stdin.readline().strip())

if length == 0:
    print(0)

else:
    n = rounding(length*0.15)
    temp = [int(sys.stdin.readline().strip()) for _ in range(length)]
    temp.sort()
    
    if n == 0:
        print(rounding(sum(temp)/len(temp)))
    
    else:
        k = temp[n:length-n] #length-n
        print(rounding(sum(k)/len(k)))