a = int(input())
temp = []

for _ in range(a):
    num = int(input())
    if num:
        temp.append(num)
    else:
        temp.pop()

print(sum(temp))

