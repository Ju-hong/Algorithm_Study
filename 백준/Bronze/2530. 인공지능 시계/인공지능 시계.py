h, m, s = map(int, input().split())
sec = int(input())

sum_time = h*60*60 + m*60 + s + sec

h_result = sum_time//3600
m_result = sum_time%3600//60
s_result = sum_time%3600%60

print(f'{h_result if h_result < 24 else h_result%24 } {m_result} {s_result}')