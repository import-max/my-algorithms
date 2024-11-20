def solution(cipher, code):      
    answer = ''
    count = len(cipher) // code
    for num in range(count):
        answer += cipher[(num+1)*code-1]
    return answer