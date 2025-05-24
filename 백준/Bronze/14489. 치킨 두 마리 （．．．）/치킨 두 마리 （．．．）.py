sum_i = sum(map(int, input().split()))
chick_two = int(input()) * 2

print(sum_i-chick_two if sum_i >= chick_two else sum_i)