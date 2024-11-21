from collections import Counter

def solution(array):
    count = Counter(array)
    sorts = count.most_common()
    
    if len(array) == 1:
        return array[0]
    if sorts[0][1] == sorts[1][1]:
        return -1
    else:
        return sorts[0][0]
    
solution([1,1,2,2])