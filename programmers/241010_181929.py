def solution(num_list):
    sums = 0
    multiply = 1
    for i in num_list:
        sums += i
        multiply *= i
    if multiply < sums*sums:
        return 1
    else:
        return 0