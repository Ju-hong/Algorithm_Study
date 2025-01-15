def solution(n):
    temp = [n]
    while n != 1:
        if n%2 != 1:
            temp.append(n/2)
            n /= 2
        else:
            temp.append(3*n + 1)
            n = 3*n + 1
    return temp

    