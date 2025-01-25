def solution(my_strings, parts):
    result = ''
    for i in range(len(my_strings)):
        a, b = parts[i][0], parts[i][1]
        result += my_strings[i][a:b+1]
    return result
        
    