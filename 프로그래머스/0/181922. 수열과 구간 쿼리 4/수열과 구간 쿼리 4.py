def solution(arr, queries):
    for s, e, k in queries:
        for n in range(s, e+1):
            if n%k == 0:
                arr[n] += 1
    return arr
                
                

             