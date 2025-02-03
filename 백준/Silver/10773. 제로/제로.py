a = int(input())
temp = []

for i in range(a):
    num = int(input())
    if num:
        temp.append(num)
    elif not num:
        temp.pop()

print(sum(temp))
