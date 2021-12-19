def solution(number):
    summ = 0
    for n in range(number):
        if n%3==0 or n%5==0:
            summ +=n
    return summ