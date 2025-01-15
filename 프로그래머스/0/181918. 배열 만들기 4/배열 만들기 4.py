def solution(arr):
    stk = [0]
    i = 0
    while i < len(arr):
        if stk[-1] >= arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1
    return stk[1:]
        