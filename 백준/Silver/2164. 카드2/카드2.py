import math


inputted = int(input())
num_square = int(math.log2(inputted))
num_mul = inputted - 2**num_square
last_num = 2 * num_mul


print(last_num if num_mul != 0 else inputted)