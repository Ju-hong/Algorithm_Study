def solution(my_string, is_suffix):
    temp = [my_string[i:] for i in range(len(my_string))]
    return 1 if is_suffix in temp else 0

        