def binary_search(sorted_list, value):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == value:
            return True
        elif sorted_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False

numbers = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
names = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(numbers, 31))
print(binary_search(numbers, 77))
print(binary_search(names, "Delta"))