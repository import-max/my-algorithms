import re

def solution(my_string):
    nums = re.findall(r"\d", my_string)
    print(nums)
    result = sum(map(int,nums))
    return result