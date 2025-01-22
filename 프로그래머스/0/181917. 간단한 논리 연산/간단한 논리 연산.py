def solution(x1, x2, x3, x4):
    if x1 | x2 : 
        x13 = True
    else:
        x13 = False
    if x3 | x4 : 
        x24 = True
    else:
        x24 = False
    if x13 & x24 :
        return True
    else:
        return False