import string

result_dict = {}

for i in string.ascii_lowercase:
    result_dict[i] = 0

for j in input().rstrip():
    result_dict[j] += 1

for key, value in result_dict.items():
    print(value, end = ' ')