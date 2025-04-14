import sys

arr = sys.stdin.readlines()

for words in arr[:-1]:
    count = 0
    for i in words:
        if i in ['a', 'e', 'i', 'o', 'u', 'I', 'A', 'E', 'O', 'U']:
            count += 1
    print(count)