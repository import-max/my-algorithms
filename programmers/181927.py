def solution(num_list):
    if num_list[-1] > num_list[-2]:
        last = num_list[-1] - num_list[-2]
    else:
        last = (num_list[-1])*2
    num_list.append(last)
    return num_list