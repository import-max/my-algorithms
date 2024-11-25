from collections import Counter

def solution(array):
    count = Counter(array)
    sorts = count.most_common()

    if len(sorts) >=2:
        if sorts[0][1] != sorts[1][1]:
            return sorts[0][0]
        else:
            return -1
    if len(array) == 1:
        return array[0]

solution([1,1])