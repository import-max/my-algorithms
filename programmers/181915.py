def solution(my_string, index_list):
    str = ''
    for i in index_list:
        str += my_string[i]
    return str