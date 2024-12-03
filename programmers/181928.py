def solution(num_list):
    # 홀수붙인수+짝수붙인수
    odd = []
    even = []
    for num in num_list:
        if num % 2 == 1:
            odd.append(str(num))
        else:
            even.append(str(num))
    odd = ''.join(odd)
    even = ''.join(even)
    return int(odd)+int(even)

