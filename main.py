import csv
import formulas


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)
        if species == '0':
            self.species = "setosa"
        elif species == '1':
            self.species = "verbosa"
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

for iris in irises:
    print(iris)

species_count = {"setosa": 0, "verbosa": 0, "virginica": 0}

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

print(formulas.find_min(sepals_len))
print(formulas.Q1(sepals_len))
print(formulas.Q3(sepals_len))


