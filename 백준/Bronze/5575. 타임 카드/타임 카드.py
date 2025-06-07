for _ in range(3):
    a, b, c, d, e, f = map(int, input().split())
    h = (d-a)*3600
    m = (e-b)*60
    times = h + m + (f-c)
    print(times//3600, times%3600//60, times%3600%60 , sep=' ')