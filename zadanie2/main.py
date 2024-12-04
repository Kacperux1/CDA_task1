import csv
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

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
# kopiowanie danych do nowej tablicy aby móc je znormalizoać jednoczesnie zachowujac dane wejsciowe
init_data_nor = init_data[:]

# Normalizujemy dane za pomoca metody MinMax {sepal_len[i] - min(selap_len)/(max(sepal_len) - min(sepal_len))}
scaler = MinMaxScaler()
scaler.fit(init_data_nor)
init_data_nor = scaler.transform(init_data_nor)

wcss = []
iteracje = []

for i in range(2, 11):
    result = KMeans(n_clusters=i, n_init=10).fit(init_data_nor)
    wcss.append(result.inertia_)
    iteracje.append(result.n_iter_)

plt.plot(range(2, 11), wcss, color="black")
plt.title('WCSS vs. Liczba klastrów')
plt.xlabel('Liczba klastrów')
plt.ylabel('WCSS')
plt.grid()
plt.show()

print(wcss)
print("")
print(iteracje)

wynik = KMeans(n_clusters=3, n_init=10).fit(init_data_nor)
init_data["group"] = wynik.labels_

wynik.cluster_centers_[:, 0] = (
            wynik.cluster_centers_[:, 0] * (max(init_data["sepal_length"]) - min(init_data["sepal_length"])) + min(
        init_data["sepal_length"]))
wynik.cluster_centers_[:, 1] = (
            wynik.cluster_centers_[:, 1] * (max(init_data["sepal_width"]) - min(init_data["sepal_width"])) + min(
        init_data["sepal_width"]))
wynik.cluster_centers_[:, 2] = (
            wynik.cluster_centers_[:, 2] * (max(init_data["petal_length"]) - min(init_data["petal_length"])) + min(
        init_data["petal_length"]))
wynik.cluster_centers_[:, 3] = (
            wynik.cluster_centers_[:, 3] * (max(init_data["petal_width"]) - min(init_data["petal_width"])) + min(
        init_data["petal_width"]))

group0 = init_data[init_data.group == 0]
group1 = init_data[init_data.group == 1]
group2 = init_data[init_data.group == 2]

plt.scatter(group0.sepal_length, group0.sepal_width, marker='o', facecolors='none', edgecolors='black')
plt.scatter(group1.sepal_length, group1.sepal_width, marker='o', facecolors='none', edgecolors='black')
plt.scatter(group2.sepal_length, group2.sepal_width, marker='o', facecolors='none', edgecolors='black')
# plt.scatter(wynik.cluster_centers_[:,0], wynik.cluster_centers_[:,1], color='black', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[0, 0], wynik.cluster_centers_[0, 1], color='orange', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[1, 0], wynik.cluster_centers_[1, 1], color='red', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[2, 0], wynik.cluster_centers_[2, 1], color='green', marker='*', s=200)
plt.title('dłogosc dzialki kielicha a szerokosc dzialki kielicha')
plt.xlabel('dłogosc dzialki kielicha')
plt.ylabel('szerokosc dzialki kielicha')
plt.show()

plt.scatter(group0.sepal_length, group0.sepal_width, color='black')
plt.scatter(group1.sepal_length, group1.sepal_width, color='black')
plt.scatter(group2.sepal_length, group2.sepal_width, color='black')
# plt.scatter(wynik.cluster_centers_[:,0], wynik.cluster_centers_[:,1], color='black', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[0, 0], wynik.cluster_centers_[0, 1], color='orange', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[1, 0], wynik.cluster_centers_[1, 1], color='red', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[2, 0], wynik.cluster_centers_[2, 1], color='green', marker='*', s=200)
plt.title('dłogosc dzialki kielicha a szerokosc dzialki kielicha')
plt.xlabel('dłogosc dzialki kielicha')
plt.ylabel('szerokosc dzialki kielicha')
plt.show()

plt.scatter(group0.sepal_length, group0.sepal_width, marker='o', facecolors='none', edgecolors='orange')
plt.scatter(group1.sepal_length, group1.sepal_width, marker='o', facecolors='none', edgecolors='red')
plt.scatter(group2.sepal_length, group2.sepal_width, marker='o', facecolors='none', edgecolors='green')
# plt.scatter(wynik.cluster_centers_[:,0], wynik.cluster_centers_[:,1], color='black', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[0, 0], wynik.cluster_centers_[0, 1], color='orange', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[1, 0], wynik.cluster_centers_[1, 1], color='red', marker='*', s=200)
plt.scatter(wynik.cluster_centers_[2, 0], wynik.cluster_centers_[2, 1], color='green', marker='*', s=200)
plt.title('dłogosc dzialki kielicha a szerokosc dzialki kielicha')
plt.xlabel('dłogosc dzialki kielicha')
plt.ylabel('szerokosc dzialki kielicha')
plt.show()

plt.scatter(group0.sepal_length, group0.sepal_width, color='orange')
plt.scatter(group1.sepal_length, group1.sepal_width, color='red')
plt.scatter(group2.sepal_length, group2.sepal_width, color='green')
plt.scatter(wynik.cluster_centers_[:, 0], wynik.cluster_centers_[:, 1], color='black', marker='*', s=200)
plt.title('dłogosc dzialki kielicha a szerokosc dzialki kielicha')
plt.xlabel('dłogosc dzialki kielicha')
plt.ylabel('szerokosc dzialki kielicha')
plt.show()


plt.scatter(group0.sepal_length, group0.petal_length, color='orange')
plt.scatter(group1.sepal_length, group1.petal_length, color='red')
plt.scatter(group2.sepal_length, group2.petal_length, color='green')
plt.scatter(wynik.cluster_centers_[:,0], wynik.cluster_centers_[:,2], color='black', marker='*', s=200)
plt.show()

plt.scatter(group0.sepal_length, group0.petal_width, color='orange')
plt.scatter(group1.sepal_length, group1.petal_width, color='red')
plt.scatter(group2.sepal_length, group2.petal_width, color='green')
plt.scatter(wynik.cluster_centers_[:,0], wynik.cluster_centers_[:,3], color='black', marker='*', s=200)
plt.show()

plt.scatter(group0.sepal_width, group0.petal_length, color='orange')
plt.scatter(group1.sepal_width, group1.petal_length, color='red')
plt.scatter(group2.sepal_width, group2.petal_length, color='green')
plt.scatter(wynik.cluster_centers_[:,1], wynik.cluster_centers_[:,2], color='black', marker='*', s=200)
plt.show()

plt.scatter(group0.sepal_width, group0.petal_width, color='orange')
plt.scatter(group1.sepal_width, group1.petal_width, color='red')
plt.scatter(group2.sepal_width, group2.petal_width, color='green')
plt.scatter(wynik.cluster_centers_[:,1], wynik.cluster_centers_[:,3], color='black', marker='*', s=200)
plt.show()

plt.scatter(group0.petal_length, group0.petal_width, color='orange')
plt.scatter(group1.petal_length, group1.petal_width, color='red')
plt.scatter(group2.petal_length, group2.petal_width, color='green')
plt.scatter(wynik.cluster_centers_[:,2], wynik.cluster_centers_[:,3], color='black', marker='*', s=200)
plt.show()

