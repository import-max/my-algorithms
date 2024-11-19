def solution(my_string):
    result = my_string[-1]
    idx = -2
    while len(result) < len(my_string):
        result += my_string[idx]
        idx -=1
    return result