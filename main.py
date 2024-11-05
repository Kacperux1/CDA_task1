import csv

import numpy as np

import formulas
import matplotlib.pyplot as plt


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

    def __repr__(self):
        return f"Iris(sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width}, species={self.species}"


irises = []

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

# for iris in irises:
# print(iris)

species_count = {"setosa": 0, "versicolor": 0, "virginica": 0}

for iris in irises:
    for key in species_count:
        if iris.species == key:
            species_count[key] += 1

print(species_count)

sepals_len = []
sepals_wid = []
petals_len = []
petals_wid = []

for iris in irises:
    sepals_len.append(iris.sepal_length)
    sepals_wid.append(iris.sepal_width)
    petals_len.append(iris.petal_length)
    petals_wid.append(iris.sepal_width)

init_sepals_len = sepals_len[:]
init_sepals_wid = sepals_wid[:]
init_petals_len = petals_len[:]
init_petals_wid = petals_wid[:]

print(formulas.find_min(sepals_len))
print(formulas.Q1(sepals_len))
print(formulas.Q3(sepals_len))

table2Date = [
    ["długosc dzialki kielicha: ", formulas.find_min(sepals_len),
     str(round(formulas.arithmetic_average(sepals_len), 2)) + "(+-" + str(
         round(formulas.standard_deviation(sepals_len), 2)) + ")",
     str(formulas.median(sepals_len)) + "(" + str(formulas.Q1(sepals_len)) + " - " + str(formulas.Q3(sepals_len)) + ")",
     formulas.find_max(sepals_len)],
    ["szerokosc dzialki kielicha: ", formulas.find_min(sepals_wid),
     str(round(formulas.arithmetic_average(sepals_wid), 2)) + "(+-" + str(
         round(formulas.standard_deviation(sepals_wid), 2)) + ")",
     str(formulas.median(sepals_wid)) + "(" + str(formulas.Q1(sepals_wid)) + " - " + str(formulas.Q3(sepals_wid)) + ")",
     formulas.find_max(sepals_wid)],
    ["długosc platka: ", formulas.find_min(petals_len),
     str(round(formulas.arithmetic_average(petals_len), 2)) + "(+-" + str(
         round(formulas.standard_deviation(petals_len), 2)) + ")",
     str(formulas.median(petals_len)) + "(" + str(formulas.Q1(petals_len)) + " - " + str(formulas.Q3(petals_len)) + ")",
     formulas.find_max(petals_len)],
    ["szerokosc platka: ", formulas.find_min(petals_wid),
     str(round(formulas.arithmetic_average(petals_wid), 2)) + "(+-" + str(
         round(formulas.standard_deviation(petals_wid), 2)) + ")",
     str(formulas.median(petals_wid)) + "(" + str(formulas.Q1(petals_wid)) + " - " + str(formulas.Q3(petals_wid)) + ")",
     formulas.find_max(petals_wid)]
]

print(table2Date)


plt.hist(sepals_len, bins=np.arange(formulas.find_min(sepals_len), formulas.find_max(sepals_len), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black', align='mid')
plt.title('Długość działki kielicha')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')
plt.show()

plt.figure()
sepals_len_by_species = [[iris.sepal_length for iris in irises if iris.species == species]
                         for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(sepals_len_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.show()

plt.hist(sepals_wid, bins=np.arange(formulas.find_min(sepals_wid), formulas.find_max(sepals_wid), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Szerokość działki kielicha')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')

plt.show()

plt.figure()
sepals_wid_by_species = [[iris.sepal_width for iris in irises if iris.species == species]
                         for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(sepals_wid_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.show()

plt.hist(petals_len, bins=np.arange(formulas.find_min(petals_len), formulas.find_max(petals_len), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Długość płatka')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')

plt.show()

plt.figure()
petal_len_by_species = [[iris.petal_length for iris in irises if iris.species == species]
                        for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(petal_len_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.title("Długość działki kielicha według gatunku")
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.show()

plt.hist(petals_wid, bins=np.arange(formulas.find_min(petals_wid), formulas.find_max(petals_wid), 0.5), alpha=0.5,
         label='Data 2', color='blue', edgecolor='black')
plt.title('Szerokość płatka')
plt.xlabel('Długość (cm)')
plt.ylabel('Liczebność')

plt.show()

plt.figure()
petal_wid_by_species = [[iris.petal_width for iris in irises if iris.species == species]
                        for species in ["setosa", "versicolor", "virginica"]]
plt.boxplot(petal_wid_by_species, vert=True, tick_labels=['Setosa', 'Versicolor', 'Virginica'])
plt.ylabel("Długość (cm)")
plt.xlabel("Gatunek")
plt.show()



corelation1 = formulas.pearson_linear_corelation(init_sepals_len, init_sepals_wid)
regression1 = formulas.linear_regression(init_sepals_len, init_sepals_wid)

plt.scatter(init_sepals_len, init_sepals_wid, color='blue')
plt.plot(np.array(init_sepals_len), regression1["a"] * np.array(init_sepals_len) + regression1["b"], color='red')
plt.title("r = " + str(round(corelation1, 2)) + "y = " + str(round(regression1["a"], 1)) + "x + " + str(round(regression1["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Szerokość działki kielicha (cm)')
plt.show()

corelation2 = formulas.pearson_linear_corelation(init_sepals_len, init_petals_len)
regression2 = formulas.linear_regression(init_sepals_len, init_petals_len)

plt.scatter(init_sepals_len, init_petals_len, color='blue')
plt.plot(np.array(init_sepals_len), regression2["a"] * np.array(init_sepals_len) + regression2["b"], color='red')
plt.title("r = " + str(round(corelation2, 2)) + "y = " + str(round(regression2["a"], 1)) + "x + " + str(round(regression2["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Długość płatka (cm)')
plt.show()

corelation3 = formulas.pearson_linear_corelation(init_sepals_len, init_petals_wid)
regression3 = formulas.linear_regression(init_sepals_len, init_petals_wid)

plt.scatter(init_sepals_len, init_petals_wid, color='blue')
plt.plot(np.array(init_sepals_len), regression3["a"] * np.array(init_sepals_len) + regression3["b"], color='red')
plt.title("r = " + str(round(corelation3, 2)) + "y = " + str(round(regression3["a"], 1)) + "x + " + str(round(regression3["b"], 1)))
plt.xlabel("Długość działki kielicha (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.show()

corelation4 = formulas.pearson_linear_corelation(init_sepals_wid, init_petals_len)
regression4 = formulas.linear_regression(init_sepals_wid, init_petals_len)

plt.scatter(init_sepals_wid, init_petals_len, color='blue')
plt.plot(np.array(init_sepals_wid), regression4["a"] * np.array(init_sepals_wid) + regression4["b"], color='red')
plt.title("r = " + str(round(corelation4, 2)) + "y = " + str(round(regression4["a"], 1)) + "x + " + str(round(regression4["b"], 1)))
plt.xlabel("Szerokość działki kielicha (cm)")
plt.ylabel('Długość płatka (cm)')
plt.show()

corelation5 = formulas.pearson_linear_corelation(init_sepals_wid, init_petals_wid)
regression5 = formulas.linear_regression(init_sepals_wid, init_petals_wid)

plt.scatter(init_sepals_wid, init_petals_wid, color='blue')
plt.plot(np.array(init_sepals_wid), regression5["a"] * np.array(init_sepals_wid) + regression5["b"], color='red')
plt.title("r = " + str(round(corelation5, 2)) + "y = " + str(round(regression5["a"], 1)) + "x + " + str(round(regression5["b"], 1)))
plt.xlabel("Szerokość działki kielicha (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.show()

corelation6 = formulas.pearson_linear_corelation(init_petals_len, init_petals_wid)
regression6 = formulas.linear_regression(init_petals_len, init_petals_wid)

plt.scatter(init_petals_len, init_petals_wid, color='blue')
plt.plot(np.array(init_petals_len), regression6["a"] * np.array(init_petals_len) + regression6["b"], color='red')
plt.title("r = " + str(round(corelation6, 2)) + "y = " + str(round(regression6["a"], 1)) + "x + " + str(round(regression6["b"], 1)))
plt.xlabel("Długość płatka (cm)")
plt.ylabel('Szerokość płatka (cm)')
plt.show()