def solution(n, control):
    for alph in control:
        if alph == 'w':
            n += 1
        elif alph == 's':
            n -= 1
        elif alph == 'd':
            n += 10
        elif alph == 'a':
            n -= 10
    return n