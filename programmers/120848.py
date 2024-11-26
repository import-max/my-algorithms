def solution(n):
    fact = 1
    cnt = 1
    while n >= fact:
        cnt += 1
        fact *= cnt
    return cnt-1