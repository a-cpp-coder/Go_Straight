def consecutive(num_arr):
    num_arr.sort()
    distance = num_arr[-1] - num_arr[0]

    return distance - len(num_arr) + 1

print(consecutive([1, 4, 5]))