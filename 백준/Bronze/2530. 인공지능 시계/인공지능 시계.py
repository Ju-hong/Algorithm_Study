h, m, s = map(int, input().split())
sec = int(input())

sum_time = h*60*60 + m*60 + s + sec

print(f'{sum_time//3600 if sum_time//3600 < 24 else sum_time//3600%24 } {sum_time%3600//60 if sum_time%3600//60 < 60 else 0} {sum_time%3600%60 if sum_time%3600%60 < 60 else 0}')
