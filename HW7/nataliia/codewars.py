##1 Count of positives / sum of negatives

# def count_positives_sum_negatives(arr):
#     if arr == []:
#         return arr
#     count_pos = 0
#     sum_neg = 0
#     for num in arr:
#         if num > 0:
#             count_pos += 1
#         else:
#             sum_neg += num
#     arr = []
#     arr.append(count_pos)
#     arr.append(sum_neg)
#     return arr



##2 Reverse List Order
# def reverse_list(l):
#     l.reverse()
#     return l


##3 Multiples of 3 or 5

# def solution(number):
#     if number < 0:
#         return 0
#     sum = 0
#     for num in range(1, number):
#         if num % 3 == 0:
#             sum += num
#         elif num % 5 == 0:
#             sum += num
#     return sum


##4 Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left


##5 Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0] == 'r' or name[0] == 'R':
#         return name + " plays banjo" 
#     else:
#         return name + " does not play banjo"


##6 Convert boolean values to strings 'Yes' or 'No'.

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"


##7 Counting sheep...

# def count_sheeps(sheep):
#     num_sh = 0
#     for s in sheep:
#         if s:
#             num_sh += 1
#     return num_sh


##8 Is this my tail?
# def correct_tail(body, tail):
#     sub = body[-1]
#     if sub == tail:
#         return True
#     else:
#         return False

