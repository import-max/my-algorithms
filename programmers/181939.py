def solution(a, b):
    ajoin = ''.join(str(a)+str(b))
    bjoin = ''.join(str(b)+str(a))
    return int(max(ajoin,bjoin))