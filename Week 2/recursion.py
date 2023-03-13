
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num,odd_sum):
    if num == 0:
        return odd_sum
    else:
        if (num % 2) == 1:
            odd_sum += num
        return loop1Rec(num - 1, odd_sum)

def loop2Rec(num,even_sum):
    if num == 20:
        return even_sum
    else:
        if num % 2 == 0:
            even_sum += num
        return loop2Rec(num + 1, even_sum)

print(loop1())
print(loop2())
# Unsure if your asking when i call it to put in the same numbers but i found this to be the easiest way.
print(loop1Rec(20,0))
print(loop2Rec(0,0))