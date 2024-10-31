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

table1Date = [
    ["długosc dzialki kielicha: ", formulas.find_min(sepals_len), str(round(formulas.arithmetic_average(sepals_len), 2))+"(+-"+str(round(formulas.standard_deviation(sepals_len), 2))+")", str(formulas.median(sepals_len))+"("+str(formulas.Q1(sepals_len))+" - "+str(formulas.Q3(sepals_len))+")", formulas.find_max(sepals_len)],
    ["szerokosc dzialki kielicha: ", formulas.find_min(sepals_wid), str(round(formulas.arithmetic_average(sepals_wid), 2))+"(+-"+str(round(formulas.standard_deviation(sepals_wid), 2))+")", str(formulas.median(sepals_wid))+"("+str(formulas.Q1(sepals_wid))+" - "+str(formulas.Q3(sepals_wid))+")", formulas.find_max(sepals_wid)],
    ["długosc platka: ", formulas.find_min(petals_len), str(round(formulas.arithmetic_average(petals_len), 2))+"(+-"+str(round(formulas.standard_deviation(petals_len), 2))+")", str(formulas.median(petals_len))+"("+str(formulas.Q1(petals_len))+" - "+str(formulas.Q3(petals_len))+")", formulas.find_max(petals_len)],
    ["szerokosc platka: ", formulas.find_min(petals_wid), str(round(formulas.arithmetic_average(petals_wid), 2))+"(+-"+str(round(formulas.standard_deviation(petals_wid), 2))+")", str(formulas.median(petals_wid))+"("+str(formulas.Q1(petals_wid))+" - "+str(formulas.Q3(petals_wid))+")", formulas.find_max(petals_wid)]
]

print(table1Date)