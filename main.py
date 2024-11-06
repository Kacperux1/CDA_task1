import csv
from ipaddress import summarize_address_range

import numpy as np

import formulas
import matplotlib.pyplot as plt


# deklaracja klasy Iris, ktora jest wykorzystywana do wczytania pliku oraz do wyliczania wartosci w punkcie 1
class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)
        if species == '0':
            self.species = "setosa"
        elif species == '1':
            self.species = "versicolor"
        else:
            self.species = "virginica"

    # reprezentacja klasy potzrebna do wczytywaja z pliku .csv
    def __repr__(self):
        return f"Iris(sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width}, species={self.species}"


irises = []
# wczytanie z pliku, z separacja
with open("data1.csv") as data:
    reader = csv.reader(data)
    for line in reader:
        sepal_length = line[0]
        sepal_width = line[1]
        petal_length = line[2]
        petal_width = line[3]
        species = line[4]
        iris = Iris(sepal_length, sepal_width, petal_length, petal_width, species)
        irises.append(iris)
# deklaracja słownika, zawierajacego liczebnosc poszczegolnych gatunkow
species_count = {"setosa": 0, "versicolor": 0, "virginica": 0}

sum = 0
# wyliczanie liczebności gatunków
for iris in irises:
    for key in species_count:
        if iris.species == key:
            species_count[key] += 1
            sum += 1
# wypisanie liczebności gatunkow wraz z udziałe procentowym i zaokrąglenie do 1 miejsca po przecinku
for key, key2 in species_count.items():
    print(f"{key} : {key2}" +"("+str("{:.1f}".format(species_count[key]*100/sum))+"%)")


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

# skopiowanie list - jest to potrzebne, poniewaz te pierwotne listy zostana posortowane i zależności zostaną zaburzone/stracone
init_sepals_len = sepals_len[:]
init_sepals_wid = sepals_wid[:]
init_petals_len = petals_len[:]
init_petals_wid = petals_wid[:]
# obliczenie i wypisanie wartosci w tabeli z punktu 1 (zaokrąglenie do 2 miejsc po przecinku)
headings = ["Cecha", "Minimum", "Śr. arytm. (+- odch. stand.)", "Mediana (Q1 - Q3)", "Maksimum"]
results_table = [
    ["Długość działki kielicha: ", "{:.2f}".format(formulas.find_min(sepals_len)),
     str("{:.2f}".format(round(formulas.arithmetic_average(sepals_len), 2))) + "(+-" + str(
         "{:.2f}".format(round(formulas.standard_deviation(sepals_len), 2))) + ")",
     str("{:.2f}".format(formulas.median(sepals_len))) + "(" + str("{:.2f}".format(formulas.Q1(sepals_len))) + " - " + str(
         "{:.2f}".format(formulas.Q3(sepals_len))) + ")",
     "{:.2f}".format(formulas.find_max(sepals_len))],
    ["Szerokość działki kielicha: ", "{:.2f}".format(formulas.find_min(sepals_wid)),
     str("{:.2f}".format(round(formulas.arithmetic_average(sepals_wid), 2))) + "(+-" + str(
         "{:.2f}".format(round(formulas.standard_deviation(sepals_wid), 2))) + ")",
     str("{:.2f}".format(formulas.median(sepals_wid))) + "(" + str("{:.2f}".format(formulas.Q1(sepals_wid))) + " - " + str(
         "{:.2f}".format(formulas.Q3(sepals_wid))) + ")",
     "{:.2f}".format(formulas.find_max(sepals_wid))],
    ["Długość płatka: ", "{:.2f}".format(formulas.find_min(petals_len)),
     str("{:.2f}".format(round(formulas.arithmetic_average(petals_len), 2))) + "(+-" + str(
         "{:.2f}".format(round(formulas.standard_deviation(petals_len), 2))) + ")",
     str("{:.2f}".format(formulas.median(petals_len))) + "(" + str("{:.2f}".format(formulas.Q1(petals_len))) + " - " + str(
         "{:.2f}".format(formulas.Q3(petals_len))) + ")",
     "{:.2f}".format(formulas.find_max(petals_len))],
    ["Szerokość płatka: ", "{:.2f}".format(formulas.find_min(petals_wid)),
     str("{:.2f}".format(round(formulas.arithmetic_average(petals_wid), 2))) + "(+-" + str(
         "{:.2f}".format(round(formulas.standard_deviation(petals_wid), 2))) + ")",
     str("{:.2f}".format(formulas.median(petals_wid))) + "(" + str("{:.2f}".format(formulas.Q1(petals_wid))) + " - " + str(
         "{:.2f}".format(formulas.Q3(petals_wid))) + ")",
     "{:.2f}".format(formulas.find_max(petals_wid))]
]
print(headings)
for item in results_table:
    print(item)
# punkt 2
# rysowanie odpowiednio histogramów oraz wykresów pudełkowych
plt.figure()
plt.hist(sepals_len, bins=np.arange((np.floor(formulas.find_min(sepals_len) * 2) / 2),
                                    (np.ceil(formulas.find_max(sepals_len) * 2) / 2 + 0.5), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black', align='mid')
plt.title('Długość działki kielicha')
plt.xticks(np.arange((np.floor(formulas.find_min(sepals_len) * 2) / 2),
                     (np.ceil(formulas.find_max(sepals_len) * 2) / 2 + 0.5), 0.5))
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')
plt.savefig("histogram_sepal_len.png", dpi=300)

plt.figure()
sepals_len_by_species = [[iris.sepal_length for iris in irises if iris.species == species]
                         for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(sepals_len_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.savefig("pudelkowy_sepal_len.png", dpi=300)

plt.figure()
plt.hist(sepals_wid, bins=np.arange((np.floor(formulas.find_min(sepals_wid) * 4) / 4),
                                    (np.ceil(formulas.find_max(sepals_wid) * 4) / 4 + 0.25), 0.25), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Szerokość działki kielicha')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')
plt.xticks(np.arange((np.floor(formulas.find_min(sepals_wid) * 4) / 4),
                     (np.ceil(formulas.find_max(sepals_wid) * 4) / 4 + 0.25), 0.25))
plt.savefig("histogram_sepal_width.png", dpi=300)

plt.figure()
sepals_wid_by_species = [[iris.sepal_width for iris in irises if iris.species == species]
                         for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(sepals_wid_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.savefig("pudelkowy_sepal_width.png", dpi=300)

plt.figure()
plt.hist(petals_len, bins=np.arange((np.floor(formulas.find_min(petals_len) * 2) / 2),
                                    (np.ceil(formulas.find_max(petals_len) * 2) / 2 + 0.5), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Długość płatka')
plt.xticks(np.arange((np.floor(formulas.find_min(petals_len) * 2) / 2),
                     (np.ceil(formulas.find_max(petals_len) * 2) / 2 + 0.5), 0.5))
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')
plt.savefig("histogram_petal_length.png", dpi=300)

plt.figure()
petal_len_by_species = [[iris.petal_length for iris in irises if iris.species == species]
                        for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(petal_len_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.savefig("pudelkowy_petal_length.png", dpi=300)

plt.figure()
plt.hist(petals_wid, bins=np.arange((np.floor(formulas.find_min(petals_wid) * 4) / 4),
                     (np.ceil(formulas.find_max(petals_wid) * 4) / 4 + 0.25), 0.25), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Szerokość płatka')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')
plt.xticks(np.arange((np.floor(formulas.find_min(petals_wid) * 4) / 4),
                     (np.ceil(formulas.find_max(petals_wid) * 4) / 4 + 0.25), 0.25))
plt.savefig("histogram_petal_width.png", dpi=300)

plt.figure()
petal_wid_by_species = [[iris.petal_width for iris in irises if iris.species == species]
                        for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(petal_wid_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.savefig("pudelkowy_petal_width.png", dpi=300)

# punkt 3 - wyliczanie współczynników regresji liniowej oraz współczynnika korelacji liniowej Pearsona
# corelationN - jest to zmienna reprezentująca współczynnik korelacji liniowej Pearsona dla danej zależności
# wyliczana z funkcji zaimplementowanj na podstawie wzoru zawartego w materiałach do zadania
# regressionN -  jest to słownik - wynik funkcji linear_regression, zawierajacy wspolczynnik kierunkowy (klucz "a") oraz wyraz wolny (klucz "b")
# wyliczone metoda najniejszych kwadratow
# oba obiekty sa zainicjalizowane osobno dla wszystkich zaleznosci

corelation1 = formulas.pearson_linear_corelation(init_sepals_len, init_sepals_wid)
regression1 = formulas.linear_regression(init_sepals_len, init_sepals_wid)

plt.figure()
plt.scatter(init_sepals_len, init_sepals_wid, color='blue')
plt.plot(init_sepals_len, regression1["a"] * np.array(init_sepals_len) + regression1["b"], color='red')
plt.title("r = " + str(round(corelation1, 2)) + " y = " + str(round(regression1["a"], 1)) + "x + " + str(
    round(regression1["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Szerokość działki kielicha (cm)')
plt.savefig("regresja1.png", dpi=300)

corelation2 = formulas.pearson_linear_corelation(init_sepals_len, init_petals_len)
regression2 = formulas.linear_regression(init_sepals_len, init_petals_len)

plt.figure()
plt.scatter(init_sepals_len, init_petals_len, color='blue')
plt.plot(init_sepals_len, regression2["a"] * np.array(init_sepals_len) + regression2["b"], color='red')
plt.title("r = " + str(round(corelation2, 2)) + " y = " + str(round(regression2["a"], 1)) + "x + " + str(
    round(regression2["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Długość płatka (cm)')
plt.savefig("regresja2.png", dpi=300)

corelation3 = formulas.pearson_linear_corelation(init_sepals_len, init_petals_wid)
regression3 = formulas.linear_regression(init_sepals_len, init_petals_wid)

plt.figure()
plt.scatter(init_sepals_len, init_petals_wid, color='blue')
plt.plot(init_sepals_len, regression3["a"] * np.array(init_sepals_len) + regression3["b"], color='red')
plt.title("r = " + str(round(corelation3, 2)) + " y = " + str(round(regression3["a"], 1)) + "x + " + str(
    round(regression3["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.savefig("regresja3.png", dpi=300)

corelation4 = formulas.pearson_linear_corelation(init_sepals_wid, init_petals_len)
regression4 = formulas.linear_regression(init_sepals_wid, init_petals_len)

plt.figure()
plt.scatter(init_sepals_wid, init_petals_len, color='blue')
plt.plot(init_sepals_wid, regression4["a"] * np.array(init_sepals_wid) + regression4["b"], color='red')
plt.title("r = " + str(round(corelation4, 2)) + " y = " + str(round(regression4["a"], 1)) + "x + " + str(
    round(regression4["b"], 1)))
plt.xlabel("Szerokość działki kielicha (cm)")
plt.ylabel('Długość płatka (cm)')
plt.savefig("regresja4.png", dpi=300)

corelation5 = formulas.pearson_linear_corelation(init_sepals_wid, init_petals_wid)
regression5 = formulas.linear_regression(init_sepals_wid, init_petals_wid)

plt.figure()
plt.scatter(init_sepals_wid, init_petals_wid, color='blue')
plt.plot(init_sepals_wid, regression5["a"] * np.array(init_sepals_wid) + regression5["b"], color='red')
plt.title("r = " + str(round(corelation5, 2)) + " y = " + str(round(regression5["a"], 1)) + "x + " + str(
    round(regression5["b"], 1)))
plt.xlabel("Szerokość działki kielicha (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.savefig("regresja5.png", dpi=300)

corelation6 = formulas.pearson_linear_corelation(init_petals_len, init_petals_wid)
regression6 = formulas.linear_regression(init_petals_len, init_petals_wid)

plt.figure()
plt.scatter(init_petals_len, init_petals_wid, color='blue')
plt.plot(init_petals_len, regression6["a"] * np.array(init_petals_len) + regression6["b"], color='red')
plt.title("r = " + str(round(corelation6, 2)) + " y = " + str(round(regression6["a"], 1)) + "x + " + str(
    round(regression6["b"], 1)))
plt.xlabel("Długość płatka (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.savefig("regresja6.png", dpi=300)
