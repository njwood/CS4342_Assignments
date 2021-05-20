import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

uploadedCSV = pd.read_csv('cars-sample.csv')

x = uploadedCSV.Weight
y = uploadedCSV.MPG

uniqueColors = {'bmw': 'purple', 'ford': 'red', 'honda': 'black', 'mercedes': 'green', 'toyota': 'yellow'}

plt.scatter(x,y, alpha=.5, c=uploadedCSV.Manufacturer.map(uniqueColors))
plt.xlim(1000,5000)
plt.ylim(10,50)
plt.xticks(np.arange(1000, 5000, step=1000))
plt.yticks(np.arange(0, 50, step=10))
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()