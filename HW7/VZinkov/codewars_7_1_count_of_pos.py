def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_pos = 0
    summ_neg = 0
    for item in arr:
        if item > 0:
            count_pos += 1
        elif item < 0:
            summ_neg += item

    return [count_pos, summ_neg]
