import re

def triple_double(num1, num2):
    str1 = str(num1)
    str2 = str(num2)

    # matches = re.findall(r"([0-9])\1{2,}", str1)
    matches_1 = re.findall(r"([0-9])\1\1", str1)
    matches_2 = re.findall(r"([0-9])\1", str2)
    intersection = set(matches_1).intersection(matches_2)

    # print(intersection == set())
    return (len(intersection) != 0)

print(triple_double(99918888, 22887))
