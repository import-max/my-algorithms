def solution(arr, n):
    if len(arr) % 2 == 0: # 짝수
        for i, ar in enumerate(arr): # 홀수 인덱스
            if i % 2 == 1:
                arr[i] = ar+n
    if len(arr) % 2 == 1: # 홀수
        for i, ar in enumerate(arr): # 짝수 인덱스
            if i % 2 == 0:
                arr[i] = ar+n
    return arr