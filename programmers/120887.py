def solution(i, j, k):
    cnt = 0
    k_str = str(k)
    for num in range(i, j+1):
        cnt += str(num).count(k_str)
    return cnt
        