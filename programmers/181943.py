def solution(my_string, overwrite_string, s):
    part1 = my_string[:s]
    if len(overwrite_string)+s == len(my_string):
        new_str = part1 + overwrite_string
    else:
        new_len = len(my_string)-len(overwrite_string)-s
        part2 = my_string[-new_len:]
        new_str = part1 + overwrite_string + part2
    return new_str