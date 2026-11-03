def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

values = [9, 4, 13, 7, 16, 2]
print(linear_search(values, 13))  
print(linear_search(values, 7))   