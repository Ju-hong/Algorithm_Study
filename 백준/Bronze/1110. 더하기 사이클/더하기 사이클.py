goal = int(input()) #인풋받은 goal 고정
num = goal # 변경해줄 num 설정
cnt = 0

while True:
    num1 = num // 10
    num2 = num % 10
    num = num2*10 + (num1 + num2)%10 
    cnt += 1

    if goal == num: 
        break
    
print(cnt)