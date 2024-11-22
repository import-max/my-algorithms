def solution(slice, n):
    cnt = 0
    if n % slice == 0:
        cnt = n // slice
    else:
        cnt = n // slice + 1
    return cnt