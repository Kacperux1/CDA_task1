from cmath import sqrt


def arithmetic_average(values):
    sum = 0
    for value in values:
        sum += values
    return sum / len(values)


def standard_deviation(values):
    temp = 0
    for value in values:
        temp += pow((value, arithmetic_average(values)), 2)
    return sqrt(1 / values.len * temp)


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
    if values.len % 2 == 0:
        return (values[values.len / 2 - 1] + values[values.len / 2]) / 2
    else:
        return values[values.len / 2]


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
