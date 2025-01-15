def solution(l, r):
    temp = []
    for num in range(l, r+1):
        TF = True
        for i in str(num): 
            if i not in ['0', '5']: #num을 str 취급 안해서
                TF = False
                break # 어디로 돌아가?
        if TF == True:
            temp.append(num)
            
    if temp:
        return temp
    else:
        return [-1]
