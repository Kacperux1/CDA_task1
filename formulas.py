from math import sqrt
from statistics import variance

def arithmetic_average(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)

def variation(values):
    temp = 0
    ar_ave = arithmetic_average(values)
    for value in values:
        temp += (value-ar_ave)**2
    return temp / len(values)

def standard_deviation(values):
    return sqrt(variation(values))


def find_max(values):
    result = 0
    for value in values:
        if value > result:
            result = value
    return result


def find_min(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def median(values):
    values.sort()
    if len(values) % 2 == 0:
        return (values[round(len(values) / 2) - 1] + values[round(len(values) / 2)]) / 2
    else:
        return values[(round(len(values) / 2))-1]


def Q1(values):
    values.sort()
    index = 0.25 * (len(values) + 1)
    if index % 1 != 0:
        return (values[int(index)] + values[int(index) + 1]) / 2
    else:
        return values[index]


def Q3(values):
    values.sort()
    index = 0.75 * (len(values) + 1)
    if index % 1 != 0:
        return (values[int(index)] + values[int(index) + 1]) / 2
    else:
        return values[index]
