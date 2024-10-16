def solution(n, slicer, num_list):
    result = []
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    if n == 1:
        result.append(num_list[:b+1])
    elif n == 2:
        result.append(num_list[a:])
    elif n == 3:
        result.append(num_list[a:b+1])
    elif n == 4:
        result.append(num_list[a:b+1:c])
    new_result = [item for nums in result for item in nums]
    return new_result