def solution(arr):
    stk = [0]
    i = 0
    while i < len(arr):
        if stk[-1] >= arr[i]: # stk에 0을 넣어주지 않으면 out of range error
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1
    return stk[1:]