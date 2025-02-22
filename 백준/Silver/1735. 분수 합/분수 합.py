def GCD(x, y):
    if x < y:
        x, y = y, x
    
    while True:
        if x % y == 0:
            return y
        else:
            x, y = y, x%y # 바로 생각나게 연습

'''
def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b  ## return의 위치에 유의
'''

i, j = map(int, input().split())
n, m = map(int, input().split())

gcd = GCD(j, m)
lcd = j*m//gcd
sumi = i*(lcd/j)+n*(lcd/m)
gcd2 = GCD(sumi, lcd)

print(int(sumi/gcd2), int(lcd/gcd2))