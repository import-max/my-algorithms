def solution(n):
    # 홀수면 n이하 홀수의 합
    add = 0
    if n % 2 == 1:
        for i in range(1,n+1,2):
            add += i

    # 짝수면 n이하 짝수의 합
    if n % 2 == 0:
        for i in range(0,n+1):
            if i % 2 == 0:
                add += i*i
    return add