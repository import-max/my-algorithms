def solution(sides):
    big = max(sides)
    sides.remove(big)
    if big < sides[0]+sides[1]:
        return 1
    else:
        return 2