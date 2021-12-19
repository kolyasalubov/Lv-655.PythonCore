def solution(numbers):
    result = 0
    for number in range(numbers):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    return result