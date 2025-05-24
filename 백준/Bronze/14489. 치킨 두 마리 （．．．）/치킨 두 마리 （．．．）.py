sum_i = sum(map(int, input().split()))
chick_two = int(input()) * 2

if sum_i >= chick_two :
    print(sum_i-chick_two)
else:
    print(sum_i)