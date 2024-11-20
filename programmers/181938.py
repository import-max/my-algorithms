def solution(a, b):
    aresult = int(''.join(str(a)+str(b)))
    bresult = 2*a*b
    if aresult == bresult:
        answer = aresult
    else:
        answer = max(aresult,bresult)
    return answer