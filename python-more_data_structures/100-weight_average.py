#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    weight_sum = 0

    for score, weight in my_list:
        avg += score * weight
        weight_sum += weight

    return avg / weight_sum
