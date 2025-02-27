def cal(a, b):
    count = 0
    while a != b:
        a, b = max(a, b) - min(a, b), min(a, b)
        count += 1
    return count

a, b = map(int, input().split())

print(int(cal(a, b)))