# Task 1 Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    counter_pos = 0
    i_neg = 0
    # if not arr:
    #     return []
    count_list = []
    if arr == [] or arr == None:
        return count_list
    for i in arr:
        if i > 0:
            counter_pos += 1
        elif i <= 0:
            i_neg += i
        else:
            return count_list
    count_list = [counter_pos, i_neg]
    return count_list


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# arr2 = []
# print(count_positives_sum_negatives(arr))
# print(count_positives_sum_negatives(arr2))

# Task 2 Reverse List Order

def reverse_list(l):
    reversed_list = l[::-1]
    return reversed_list


# print(reverse_list([1, 2, 3, 4]))

# Task 3 Multiples of 3 or 5

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0 and i >= 0:
            sum += i
    return sum


# print(solution(20))

# Task 4 Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg < fuel_left:
        return True
    else:
        return False

# Task 5 Are You Playing Banjo?


def are_you_playing_banjo(name):
    for i in name:
        if i == "R" or i == "r":
            return name + " plays banjo"
        else:
            return name + " does not play banjo"

# Task 6 Convert boolean values to strings 'Yes' or 'No'.


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

# Task 7 Counting sheep...


def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

# Сподобався варіант розв'язку
# def count_sheeps(x):
#   return x.count(True)

# Task 8 Is this my tail?


def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False

# Сподобався варіант
# def correct_tail(body, tail):
#     return body[-1] == tail
