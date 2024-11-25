def solution(rsp):
    result = ''
    for i in rsp:
        if i == '2':
            result += '0'
        if i == '0':
            result += '5'
        if i == '5':
            result += '2'
    return result