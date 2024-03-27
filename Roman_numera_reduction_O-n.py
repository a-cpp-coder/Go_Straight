# input: "DDLL"

def RomanNumeralReduction(strParam):
    decimal = [1, 5, 10, 50, 100, 500, 1000]
    roman   = ["I", "V", "X", "L", "C", "D", "M"]

    sum = 0
    result = ""
    # not work this way because of you still need the index of the "character"
    # for i, v in enumerate(strParam):
    #     print(i)
    #     sum += decimal[i]
    for i in strParam:
        sum += decimal[roman.index(i)]

    decimal.reverse()
    roman.reverse()

    for i in decimal:
        if sum >= i:
            n = sum // i
            # print(type(n))
            result += roman[decimal.index(i)] * n  # just go ahead and finish 1st before optimizing
            sum -= n * i
        else:
            continue
    
    return result


# def RomanNumeralReduction(strParam):
#   decimal = [1, 5, 10, 50, 100, 500, 1000]
#   roman   = ["I", "V", "X", "L", "C", "D", "M"]

#   number = 0
#   for i in strParam:
#     number += decimal[roman.index(i)]

#   decimal.reverse()
#   roman.reverse()
#   result = ""
#   for i in decimal:
#     if number < i:
#       continue
#     else:
#       while number >= i:
#         number -= i
#         result += roman[decimal.index(i)]


#   # code goes here
#   return result

# keep this function call here 
print(RomanNumeralReduction("XXXVVIIIIIIIIII"))
# "XXXVVIIIIIIIIII"