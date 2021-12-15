def solution(number):
    if number<3:
        return 0
    sum=0 
    num=3
    while num<number:
        if num%3==0 or num%5==0:
            sum+=num
        num+=1
    return sum    