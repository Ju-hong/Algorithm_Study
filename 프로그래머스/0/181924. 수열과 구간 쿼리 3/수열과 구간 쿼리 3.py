def solution(arr, queries):
    for query in queries:
        num1 = arr[query[0]]
        num2 = arr[query[1]]
        arr[query[0]] = num2
        arr[query[1]] = num1 
    return arr


        
        
