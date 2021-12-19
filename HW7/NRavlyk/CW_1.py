# не пройшов
def count_positives_sum_negatives(arr):
    retsumm = [0,0]
    for number in arr:
        if number>0:
            retsumm[0] += number 
        else:
            retsumm[1] += number 
    return retsumm

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))