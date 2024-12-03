def solution(my_string, alp):
    ALP = alp.upper()
    if alp in my_string:
        my_string = my_string.replace(alp, ALP)
    return my_string

