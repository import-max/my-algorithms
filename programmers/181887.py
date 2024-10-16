def solution(num_list):
    hol = 0
    jjak = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 1:
            hol += num
        else:
            jjak += num
    return max(hol,jjak)