def solution(num_list):
    add = []
    even = []
    answer = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            add.append(num)
    answer.append(len(even))
    answer.append(len(add))
    return answer