import random

# The time complexity of this algorithm is O(n) because it needs to iterate through the entire list once.
def shuffle_list(list):
    n = len(list)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        list[i], list[j] = list[j], list[i]
    return list

# Sample Input
list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

# Display list before shuffle
print("Before Shuffle:\n", list)
print("Shuffled:\n",shuffle_list(list))
print(shuffle_list(list))
print(shuffle_list(list))
print(shuffle_list(list))
print(shuffle_list(list))
