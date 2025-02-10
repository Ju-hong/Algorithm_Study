import sys

def calcul(x):
    n, m = map(int, x.split())
    
    for i in range(n, m+1): # 3 16
        
        if i == 1:
            continue
        
        for j in range(2, int(i**0.5)+1):

            if i % j == 0:
                break
                
        else:
            print(i)


calcul(sys.stdin.readline().strip())