import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import algorithm


# Wczytanie danych
class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)


init_data = pd.read_csv("data2.csv", header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width"])

# Normalizacja danych
scaler = MinMaxScaler()
scaler.fit(init_data)
init_data_nor = scaler.transform(init_data)

# WCSS i liczba iteracji dla różnych liczby klastrów
wcss = []
iterations = []

for i in range(2, 11):
    result = algorithm.CustomKMeans(i, init_data_nor, 0.00001)
    wcss.append(result.wcss)
    iterations.append(result.iteration_number)

# Wykres WCSS
plt.plot(range(2, 11), wcss, color="black")
plt.title('WCSS vs. Liczba klastrów')
plt.xlabel('Liczba klastrów')
plt.ylabel('WCSS')
plt.grid()
plt.savefig("wcss_od_liczby_klastrow", dpi=300)
plt.show()

print("WCSS:", wcss)
print("Iterations:", iterations)

result = algorithm.CustomKMeans(3, init_data_nor, 0.00001)

init_data["group"] = result.groups

group0 = init_data[init_data.group == 0]
group1 = init_data[init_data.group == 1]
group2 = init_data[init_data.group == 2]

centers = np.array(result.centers)

centers[:, 0] = (
        centers[:, 0] * (max(init_data["sepal_length"]) - min(init_data["sepal_length"])) + min(
    init_data["sepal_length"]))
centers[:, 1] = (
        centers[:, 1] * (max(init_data["sepal_width"]) - min(init_data["sepal_width"])) + min(
    init_data["sepal_width"]))
centers[:, 2] = (
        centers[:, 2] * (max(init_data["petal_length"]) - min(init_data["petal_length"])) + min(
    init_data["petal_length"]))
centers[:, 3] = (
        centers[:, 3] * (max(init_data["petal_width"]) - min(init_data["petal_width"])) + min(
    init_data["petal_width"]))



plt.scatter(group0.sepal_length, group0.sepal_width, color='orange')
plt.scatter(group1.sepal_length, group1.sepal_width, color='red')
plt.scatter(group2.sepal_length, group2.sepal_width, color='green')
plt.scatter(centers[:, 0], centers[:, 1], color='black', marker='*', s=200)
plt.title('długośc działki kielicha a szerokość działki kielicha')
plt.xlabel('długość działki kielicha')
plt.ylabel('szerokość działki kielicha')
plt.savefig("sepal_len_sepal_wid.png", dpi=300)
plt.show()

plt.scatter(group0.sepal_length, group0.petal_length, color='orange')
plt.scatter(group1.sepal_length, group1.petal_length, color='red')
plt.scatter(group2.sepal_length, group2.petal_length, color='green')
plt.scatter(centers[:, 0], centers[:, 2], color='black', marker='*', s=200)
plt.title('długośc działki kielicha a długość płatka')
plt.xlabel('długość działki kielicha')
plt.ylabel('długość płatka')
plt.savefig("sepal_len_petal_len.png", dpi=300)
plt.show()

plt.scatter(group0.sepal_length, group0.petal_width, color='orange')
plt.scatter(group1.sepal_length, group1.petal_width, color='red')
plt.scatter(group2.sepal_length, group2.petal_width, color='green')
plt.scatter(centers[:, 0], centers[:, 3], color='black', marker='*', s=200)
plt.title('długośc działki kielicha a szerokość płatka')
plt.xlabel('długość działki kielicha')
plt.ylabel('szerokość płatka')
plt.savefig("sepal_len_petal_wid.png", dpi=300)
plt.show()

plt.scatter(group0.sepal_width, group0.petal_length, color='orange')
plt.scatter(group1.sepal_width, group1.petal_length, color='red')
plt.scatter(group2.sepal_width, group2.petal_length, color='green')
plt.scatter(centers[:, 1], centers[:, 2], color='black', marker='*', s=200)
plt.title('szerokość działki kielicha a długość płatka')
plt.xlabel('szerokość działki kielicha')
plt.ylabel('długość płatka')
plt.savefig("sepal_wid_petal_len.png", dpi=300)
plt.show()

plt.scatter(group0.sepal_width, group0.petal_width, color='orange')
plt.scatter(group1.sepal_width, group1.petal_width, color='red')
plt.scatter(group2.sepal_width, group2.petal_width, color='green')
plt.scatter(centers[:, 1], centers[:, 3], color='black', marker='*', s=200)
plt.title('szerokość działki kielicha a szerokość płatka')
plt.xlabel('szerokość działki kielicha')
plt.ylabel('szerokość płatka')
plt.savefig("sepal_wid_petal_wid.png", dpi=300)
plt.show()

plt.scatter(group0.petal_length, group0.petal_width, color='orange')
plt.scatter(group1.petal_length, group1.petal_width, color='red')
plt.scatter(group2.petal_length, group2.petal_width, color='green')
plt.scatter(centers[:, 2], centers[:, 3], color='black', marker='*', s=200)
plt.title('długość płatka a szerokość płatka')
plt.xlabel('długość płatka')
plt.ylabel('szerokość płatka')
plt.savefig("petal_len_petal_wid.png", dpi=300)
plt.show()
