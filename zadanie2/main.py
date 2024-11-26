import csv

import formulas2

# deklaracja klasy Iris, ktora jest wykorzystywana do wczytania pliku oraz do wyliczania wartosci w punkcie 1
class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)


irises = []
# wczytanie z pliku, z separacja
with open("data2.csv") as data:
    reader = csv.reader(data)
    for line in reader:
        sepal_length = line[0]
        sepal_width = line[1]
        petal_length = line[2]
        petal_width = line[3]
        iris = Iris(sepal_length, sepal_width, petal_length, petal_width)
        irises.append(iris)

# deklaracja list, ktore beda zawierały poszczegolne wartosci mierzone
sepals_len = []
sepals_wid = []
petals_len = []
petals_wid = []

# wczytanie wartosci do list
for iris in irises:
    sepals_len.append(iris.sepal_length)
    sepals_wid.append(iris.sepal_width)
    petals_len.append(iris.petal_length)
    petals_wid.append(iris.petal_width)

sepals_len_normalized = sepals_len[:]
sepals_wid_normalized = sepals_wid[:]
petals_len_normalized = petals_len[:]
petals_wid_normalized = petals_wid[:]
formulas2.normalization(sepals_len_normalized)
formulas2.normalization(sepals_wid_normalized)
formulas2.normalization(petals_len_normalized)
formulas2.normalization(petals_wid_normalized)

print(sepals_len)
print(sepals_wid)
print(petals_len)
print(petals_wid)

print("")

print(sepals_len_normalized)
print(sepals_wid_normalized)
print(petals_len_normalized)
print(petals_wid_normalized)
