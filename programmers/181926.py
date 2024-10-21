def solution(n, control):
    w_cnt = control.count('w')
    s_cnt = control.count('s')
    d_cnt = control.count('d')
    a_cnt = control.count('a')
    sum_cnt = ((d_cnt - a_cnt) * 10) + w_cnt - s_cnt
    return sum_cnt + n