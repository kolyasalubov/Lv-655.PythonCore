def solution(number):
    set_1 = set()
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            set_1.add(num)
    return sum(set_1)
