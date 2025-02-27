def strings(x):
    x = str(x)
    return x == x[::-1] 

def cal(x):
    if x <2:
        return False 
    
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True 

x = int(input())

while True:
    if strings(x) & cal(x):
        break
    else:
        x += 1
    
print(x)