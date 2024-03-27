def find_intersection(strArr):
    str_1 = strArr[0]
    str_2 = strArr[1]

    list_1 = list(map(int, str_1.split(", ")))
    list_2 = list(map(int, str_2.split(", ")))
    result = []
    print(list_1)
    print(list_2)
    i, j = 0, 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] == list_2[j]:
            result.append(list_1[i])
            i += 1
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        elif list_1[i] > list_2[j]:
            j += 1

    # experience mean take the mistakes sooner, and dare to change, 
    # only condition inverse shoud use separate if, others should be elif
        # if list_1[i] < list_2[j]:
        #     i += 1
        # if list_1[i] > list_2[j]:
        #     j += 1
    # We need test a coverage cases because the Dev make mistakes
    # just calm and note down the algor
    return result

print(find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))