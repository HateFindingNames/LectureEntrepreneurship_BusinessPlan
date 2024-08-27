import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

efile = "\\elektr_nhk_ab-2007.tsv"
gfile = "\\gas_nhk_ab-2007.tsv"

# heads = ["Freq", "Product"]

class data_dict(dict):
    "https://stackoverflow.com/a/57006277"
    def __init__(self):
        self = dict()
    def add(self, key, value):
        for i, val in enumerate(value):
            if val == ":":
                value[i] = np.NaN
        self[key] = value

# read in tsv and store as pandas dataframe 'edf'
with open(os.path.dirname(__file__)+efile, "r") as e:
    ctry = data_dict()
    for i, line in enumerate(e.readlines()):
        line = line.strip()
        line = line.split(sep="\t")
        line = [x.strip().replace(" e", "").replace(" p", "") for x in line]
        line[0] = line[0].split(sep=",")
        if i == 0:
            heads = line
            properties = heads[0]
            properties[-1] = "geo"
            continue
        # elif i == 1:
        #     print(properties)
        #     print(line)
        ctry.key = line[0][-1]
        ctry.value = line[1:]
        ctry.add(ctry.key, ctry.value)
    
edf = pd.DataFrame.from_dict(ctry, dtype="float")
# print(edf)
# print(heads)

xlabel = "Zeitperioden"
ylabel = "Euro pro kWh"
title = "Titel"
fig, ax = plt.subplots(1,1,figsize=(10, 5))

countries = edf.columns
for country in countries:
    ax.plot(heads[1:], edf[country], "-o", markersize=.5, label=country)
ax.legend()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.tick_params(axis='x', labelrotation=45)
ax.set_ylim(ymin=0, ymax=.8)
plt.tight_layout()
plt.show()
# print(heads[1:])
# print(len(edf["AL"]))