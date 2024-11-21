from math import sqrt
import numpy as np


# Autorzy - Kacper Maziarz 251586, Jędrzej Bartoszewski 251482

# wyliczanie średniej arytmetycznej
def arithmetic_average(values):
    total = 0
    for value in values:
        total += value

    return total / len(values)


# funkcja obliczajaca wariancję
def variance(values):
        temp = 0
        avg = arithmetic_average(values)
        for value in values:
            temp += (value - avg) ** 2
        return temp / (len(values) -1)

#odchylenie standardowe z wariancji
def standard_deviation(values):
    return sqrt(variance(values))

#funkcja obliczajaca kowariancję (wariancję dwóch zbiorów)
#zakładamy, że są to dwa niepuste zbiory o takiej samej liczności
def covariance(x_values, y_values):
    result = 0
    for i in range(len(x_values)):
        result += (x_values[i] - arithmetic_average(x_values))*(y_values[i] - arithmetic_average(y_values))
    return result / (len(x_values)-1)

# znajdowanie wartości maksymalnej
def find_max(values):
    result = 0
    for value in values:
        if value > result:
            result = value
    return result

#znajdowanie wartości minimalnej
def find_min(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result

#obliczanie mediany dla obu przypadków liczności zbioru
def median(values):
    values.sort()
    if len(values) % 2 == 0:
        return (values[len(values) // 2 - 1] + values[len(values) // 2 ] ) / 2
    else:
        return values[(np.ceil(len(values) / 2)) - 1]

#obliczanie pierwszego kwartyla
def Q1(values):
    values.sort()
    index = 0.25 * (len(values) + 1)
    if index % 1 != 0:
        return (values[int(index)] + values[int(index) + 1]) / 2
    else:
        return values[index]

#obliczanie tzreciego kwartyla
def Q3(values):
    values.sort()
    index = 0.75 * (len(values) + 1)
    if index % 1 != 0:
        return (values[int(index)] + values[int(index) + 1]) / 2
    else:
        return values[index]

#obliczanie współczynników regresji liniowej metoda najmniejszych kwadratów (na podstawie wzoru z materiałów)
def linear_regression(x_values, y_values):
    result = {"a": 0, "b": 0}

    result["a"] = covariance(x_values, y_values) / variance(x_values)
    result["b"] = arithmetic_average(y_values) - result["a"] * arithmetic_average(x_values)
    return result



#współczynnik korelacji liniowej Pearsona (na podst. wzoru z materiałów)
def pearson_linear_corelation(x_values, y_values):
    return covariance(x_values, y_values) / (standard_deviation(x_values)*standard_deviation(y_values))



