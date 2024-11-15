import re

def solution(babbling):
    pattern = re.compile(r"^(aya|ye|woo|ma)+")
    count = 0
    for word in babbling:
        if pattern.fullmatch(word):
            count += 1
    return count