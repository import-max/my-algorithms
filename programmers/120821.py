def solution(num_list):
    result = []
    for num in range(len(num_list)):
        result.append(num_list[-num-1])
    return result