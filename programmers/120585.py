def solution(array, height):
    cnt = 0
    for arr in array:
        if arr > height:
            cnt += 1
    print(cnt)
    return cnt

solution([170,170,180],165)