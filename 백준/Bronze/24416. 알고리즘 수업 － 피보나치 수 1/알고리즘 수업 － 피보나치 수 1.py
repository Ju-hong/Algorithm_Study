def fibo1(n):
    global count1 
    if n == 1 or n ==2 :
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)


def fibo2(n):
    count2= 0
    f = [0]*(n+1) # index 어렵다
    f[1], f[2] = 1, 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2] 
        count2 += 1
    return count2


n = int(input())


print(fibo1(n), fibo2(n))
