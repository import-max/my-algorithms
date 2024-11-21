def solution(array):
    array.sort()
    count = len(array) // 2 
    return array[count]