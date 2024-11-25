def solution(n):
    answer = 1
    if n % 6 == 0:
        answer = n // 6
    else:
        while (6*answer) % n != 0:
            answer += 1
    return answer