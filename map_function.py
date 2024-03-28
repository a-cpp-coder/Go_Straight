numbers = [0, 2, 4, 6, 8]

def square(x):
    return x ** 2
test = map(square, numbers)
print(list(test))

# case 2
numbers1 = [0, 2, 4, 6, 8]
numbers2 = [1, 3, 5, 7, 9]
test2 = map(lambda x, y: x + y, numbers1, numbers2)
print(list(test2))
# or
add = lambda x, y: x + y
test3 = map(add, numbers1, numbers2)