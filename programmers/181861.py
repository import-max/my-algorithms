def solution(arr):
    result = []
    for idx, num in enumerate(arr):
        for n in range(num):
            result.append(arr[idx])
    return result