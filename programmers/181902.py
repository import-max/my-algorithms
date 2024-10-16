def solution(my_string):
    sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = []
    for i in sample:
        cnt = my_string.count(i)
        result.append(cnt)
    return result