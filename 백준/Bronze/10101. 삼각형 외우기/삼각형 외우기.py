import sys
n, m, k = map(int, sys.stdin.readlines())

if n == m == k == 60:
    print("Equilateral")
elif (n + m + k) != 180:
    print("Error")
elif (n != m) & (n != k) & (m != k):
    print("Scalene")
else:
    print("Isosceles")