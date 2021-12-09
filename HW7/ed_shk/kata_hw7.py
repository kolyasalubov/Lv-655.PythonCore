"""
Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array.
"""
def count_positives_sum_negatives(arr):
    if arr:
        d = {"count": 0, "sum": 0}
        for element in arr:
            if element > 0:
                d["count"] = d["count"] + 1
            else:
                d["sum"] = d["sum"] + element
        return list(d.values())
    else:
        return []

"""
In this kata you will create a function that takes in a list and returns a list with the reverse order.
"""
def reverse_list(l):
    return l[::-1]

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 
(for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
"""
def solution(number):
    y = set()
    [y.add(num) for num in range(1, number) if num % 3 == 0 or num % 5 == 0]
    return sum(y)

"""
You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. 
There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. 
Function should return true (1 in Prolog and NASM) 
if it is possible and false (0 in Prolog and NASM) if not. The input values are always positive.
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left * mpg >= distance_to_pump else False

"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"
"""
def are_you_playing_banjo(name):
    return name + ' plays banjo' if name[0] == 'R' or name[0] == 'r' else name + " does not play banjo"

"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

"""
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).
"""
def count_sheeps(sheep):
    return sheep.count(True)

"""
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
If the tail is right return true, else return false.
The arguments will always be strings, and normal letters.
"""
def correct_tail(body, tail):
     return True if body[-1] == tail[0] else False


