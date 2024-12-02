def solution(n):
    result = 0
    numlist = list(str(n))
    for num in numlist:
        result += int(num)
    return result
