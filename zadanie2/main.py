import csv
from sklearn.cluster import KMeans
import formulas2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# deklaracja klasy Iris, ktora jest wykorzystywana do wczytania pliku oraz do wyliczania wartosci w punkcie 1
class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)

init_data = pd.read_csv("data2test.csv")

"""
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

data = {
    "sepal_len": sepals_len,
    "sepal_wid": sepals_wid,
    "petal_len": petals_len,
    "petal_wid": petals_wid,
}

sepals_len_normalized = sepals_len[:]
sepals_wid_normalized = sepals_wid[:]
petals_len_normalized = petals_len[:]
petals_wid_normalized = petals_wid[:]
formulas2.normalization(sepals_len_normalized)
formulas2.normalization(sepals_wid_normalized)
formulas2.normalization(petals_len_normalized)
formulas2.normalization(petals_wid_normalized)

data_nor = {
    "sepal_len_nor": sepals_len_normalized,
    "sepal_wid_nor": sepals_wid_normalized,
    "petal_len_nor": petals_len_normalized,
    "petal_wid_nor": petals_wid_normalized,
}

data_nor_arr = []
for i in range(len(sepals_len_normalized)):
    data_nor_arr.append([sepals_len_normalized[i], sepals_wid_normalized[i], petals_len_normalized[i], petals_wid_normalized[i]])

wynik = KMeans(n_clusters=3, n_init=10).fit(data_nor_arr)

data["group"] = wynik.labels_
data_nor["group"] = wynik.labels_

effect = pd.DataFrame(data)
effect_nor = pd.DataFrame(data_nor)

print(effect)
print(effect_nor)

group0 = effect_nor[effect_nor.group == 0]
group1 = effect_nor[effect_nor.group == 1]
group2 = effect_nor[effect_nor.group == 2]
"""

wynik = KMeans(n_clusters=3, n_init=10).fit(init_data)
init_data["group"] = wynik.labels_

group0 = init_data[init_data.group == 0]
group1 = init_data[init_data.group == 1]
group2 = init_data[init_data.group == 2]

plt.scatter(group0.sepal_length, group0.sepal_width, color='blue')
plt.scatter(group1.sepal_length, group1.sepal_width, color='red')
plt.scatter(group2.sepal_length, group2.sepal_width, color='green')
plt.show()
