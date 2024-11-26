from math import sqrt
import numpy as np


# Autorzy - Kacper Maziarz 251586, Jędrzej Bartoszewski 251482

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


#funkcja normalizująca dane - wartosci wyjsciowe sa z zakresu 0-1
def normalization(values):
    minimal = find_min(values)
    maximal = find_max(values)
    for i in range(len(values)):
        values[i] = (values[i] - minimal)/(maximal - minimal)
    return values




