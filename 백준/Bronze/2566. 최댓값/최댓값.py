listing = []

listing += [list(map(int, input().split())) for _ in range(9)]

maxi = max(listing[i][j] for i in range(9) for j in range(9))

for i in range(9):
    for j in range(9):
        if listing[i][j] == maxi:
            print(maxi)
            print(i+1, j+1)
            break
