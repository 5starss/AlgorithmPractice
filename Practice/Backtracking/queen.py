def solution(my_string, overwrite_string, s):
    return my_string.replace(my_string[s:s+len(overwrite_string) if len(overwrite_string) < len(my_string) - s else len(my_string)], overwrite_string)

print(solution("He11oWor1d", "lloWorl", 2))
