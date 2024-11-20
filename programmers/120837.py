def solution(hp):
    ants = [5,3,1]
    count = 0
    
    for ant in ants:
        count += hp // ant
        hp %= ant
        
    return count if hp ==0 else -1