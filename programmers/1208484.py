def solution(chicken):
    count = 0
    while chicken >= 10:                            
        free = chicken // 10                        
        count += free                             
        chicken = free + (chicken % 10)             
    return count