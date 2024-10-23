def solution(str1, str2):
    result = []
    for i,j in zip(str1, str2):
        result.append(i)
        result.append(j)
    return ''.join(result)