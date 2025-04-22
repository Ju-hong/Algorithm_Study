import string

lower = [i for i in string.ascii_lowercase]
result = [-1]*len(lower)
count = 0 

for i in input().rstrip():
    if result[lower.index(i)] == -1:
        result[lower.index(i)] = count
    count += 1

print(' '. join(list(map(str, result))))