# Have the function BinaryConverter(str) return the decimal form of the binary value. For example: if 101 is passed return 5, or if 1000 is passed return 8.
def binary_converter(str_param):
    return int(str_param, 2)

print(binary_converter("10111"))