from math import sqrt
from statistics import variance


def arithmetic_average(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)



def variance(values):
    temp = 0
    avg = arithmetic_average(values)
    for value in values:
        temp += (value - avg) ** 2
    return temp / (len(values) -1)


def standard_deviation(values):
    return sqrt(variance(values))

def covariance(x_values, y_values):
    result = 0
    for i in range(len(x_values)):
        result += (x_values[i] - arithmetic_average(x_values))*(y_values[i] - arithmetic_average(y_values))
    return result / (len(x_values)-1)


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
        return values[(round(len(values) / 2)) - 1]


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


def linear_regression(x_values, y_values):
    result = {"a": 0, "b": 0}

    result["a"] = covariance(x_values, y_values) / variance(x_values)
    result["b"] = arithmetic_average(y_values) - result["a"] * arithmetic_average(x_values)
    return result




def pearson_linear_corelation(x_values, y_values):
    return covariance(x_values, y_values) / (standard_deviation(x_values)*standard_deviation(y_values))



