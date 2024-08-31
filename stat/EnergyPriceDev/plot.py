import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('ticks') # setting style
# sns.set_context('paper') # setting context

efile = "\\elektr_nhk_ab-2007.tsv"
gfile = "\\gas_nhk_ab-2007.tsv"

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
        line = [x.strip().replace(" e", "").replace(" p", "").replace(" d", "").replace(" c", "") for x in line]
        line[0] = line[0].split(sep=",")
        if i == 0:
            heads = line
            properties = heads[0]
            properties[-1] = "geo"
            continue
        elif line[0][5] == "EUR" and line[0][4] == "X_TAX" and line[0][3] == "KWH" and line[0][2] == "MWH20-499":
            # print(line)
            ctry.key = line[0][-1]
            ctry.value = line[1:]
            ctry.add(ctry.key, ctry.value)

edf = pd.DataFrame.from_dict(ctry, dtype="float")

with open(os.path.dirname(__file__)+gfile, "r") as g:
    ctry = data_dict()
    for i, line in enumerate(g.readlines()):
        line = line.strip()
        line = line.split(sep="\t")
        line = [x.strip().replace(" e", "").replace(" p", "").replace(" d", "").replace(" c", "") for x in line]
        line[0] = line[0].split(sep=",")
        if i == 0:
            heads = line
            properties = heads[0]
            properties[-1] = "geo"
            continue
        elif line[0][5] == "EUR" and line[0][4] == "X_TAX" and line[0][3] == "GJ_GCV" and line[0][2] == "GJ1000-9999":
            ctry.key = line[0][-1]
            ctry.value = line[1:]
            ctry.add(ctry.key, ctry.value)
    
gdf = pd.DataFrame.from_dict(ctry, dtype="float")

xlabel = ""
ylabel = "Euro pro kWh"
ylabel2 = "Euro pro GJ"
title = "Industriepreisentwicklung Elektrizität und Gas ex Steuer\nwichtiger Länder in der EU"

fig, ax = plt.subplots(1,1,figsize=(10, 5))

countries = [
    "DE",
    "ES",
    "FR",
    "IT",
    "AT"
]

ax2 = ax.twinx()
for country in countries:
    ax.plot(heads[1:], edf[country], "-o", markersize=0, lw=.75, label=country, linestyle="--")
    ax2.plot(heads[1:], gdf[country], "-o", markersize=0, lw=.75, label=country)
for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax.legend(title="Elektrizität", loc="upper left")
ax2.legend(title="Gas", loc="lower left")

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax2.set_ylabel(ylabel2)
ax.set_title(title)
ax.tick_params(axis='x', labelrotation=30)
ax.set_ylim(ymin=0.05, ymax=.4)
ax2.set_ylim(ymin=0, ymax=35)
ax.grid(axis="both", alpha=.5)
plt.tight_layout()
# plt.show()
plt.savefig("stat/EnergyPriceDev/eg_prices_eu.svg")