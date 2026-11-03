def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

values = [10, 4, 12, 8]
print(linear_search(values, 12))  # 2