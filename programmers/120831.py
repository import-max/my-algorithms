def solution(n):
    nsum = 0
    for i in range(n+1):
        if i % 2 == 0:
            nsum+= i
    return nsum
