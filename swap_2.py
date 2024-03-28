import re

def swap_2(str_param):
    str1 = [char.lower if 65 <= ord(char) <= 90 else char.upper() for char in str_param]
    str1 = "".join(str1)

    result = ""
    matches = re.findall(r"([0-9][a-zA-Z]+[0-9])", str1)  # yes num + #letter + num
    for match in matches:
        first_num = match[0]
        letters = match[1:-1]
        last_num = match[-1]
        result += last_num + letters + first_num

    return result

print(swap_2("6coderbyte5"))

