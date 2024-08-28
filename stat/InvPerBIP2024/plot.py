import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('ticks') # setting style
# sns.set_context('paper') # setting context

ifile = "\\estat_tec00132.tsv"

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
with open(os.path.dirname(__file__)+ifile, "r") as e:
    bsn = data_dict()
    gov = data_dict()
    for i, line in enumerate(e.readlines()):
        line = line.strip()
        line = line.split(sep="\t")
        # removing flags: (p) provisional, (e) estimated, (b) break in time series, (d) definition differs
        line = [x.strip().replace(" e", "").replace(" p", "").replace(" d", "").replace(" c", "") for x in line]
        line[0] = line[0].split(sep=",")
        if i == 0:
            heads = line
            properties = heads[0]
            properties[-1] = "geo"
            continue
        elif line[0][2] == "INV_BSN":
            bsn.key = line[0][-1]
            bsn.value = line[1:]
            bsn.add(bsn.key, bsn.value)
        elif line[0][2] == "INV_GOV":
            # print(line)
            gov.key = line[0][-1]
            gov.value = line[1:]
            gov.add(gov.key, gov.value)

bsndf = pd.DataFrame.from_dict(bsn, dtype="float")
govdf = pd.DataFrame.from_dict(gov, dtype="float")
# print(gov)

xlabel = "Jahr"
ylabel = "\% BIP"
title = "Bruttoanlageninvestitionen (BAI) in Prozent des BIP"

fig, ax = plt.subplots(1,1,figsize=(10, 5))

# countries = edf.columns
countries = [
    "DE",
    "ES",
    "FR",
    "IT",
    "AT"
]

for country in countries:
    ax.plot(heads[1:], bsndf[country], lw=.75, label=f"{country} (BSN)", linestyle="--")
for country in countries:
    ax.plot(heads[1:], govdf[country], lw=1, label=f"{country} (GOV)")

ax.legend(loc="upper left")
# ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.tick_params(axis='x', labelrotation=45)
# ax.set_ylim(ymin=0.05, ymax=.4)
plt.tight_layout()
# plt.show()
plt.savefig("stat/InvPerBIP2024/InvPerBIP2024.svg")