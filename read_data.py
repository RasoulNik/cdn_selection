import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
# file = open('5gsolutions-dataset-uc4-2.csv')
# csvreader = csv.reader(file)
# rows = []
# for row in csvreader:
#         rows.append(row)
# data = []
# for row in rows[1:]:
#         data
# data = np.array(rows[1:])
# np.mean(data)
data= pd.read_csv('102-edge-final.csv')

bw = data.get("bw")

np.mean(bw)
np.std(bw)
plt.plot(bw)
plt.show()