import math

def number_search(str_p):
    digits = [i for i in str_p if i.isdigit()]
    number_of_digits = sum(int(i) for i in digits)

    letters = [j for j in str_p if j.isalpha()]
    number_of_letters = len(letters)

    result = number_of_digits / number_of_letters

    if result > math.floor(result) + 0.5:
        result = math.ceil(result)
    else:
        result = math.floor(result)
    
    return result

print(number_search("3Hello9 9 9"))


