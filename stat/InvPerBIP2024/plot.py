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
ylabel = "BAI in Mrd. €"
title = "Gewerbliche (BSN) und staatliche (GOV) Bruttoanlageninvestitionen (BAI) nach EU-Land"

fig, ax = plt.subplots(1,1,figsize=(10, 5))

# countries = edf.columns
countries = [
    "DE",
    "ES",
    "FR",
    "IT",
    "AT"
]

# absolute BIPs 2012 to 2023
bips = {
    "DE": [2800.4, 2867.3, 2985.2, 3085.7, 3196.1, 3331.1, 3431.1, 3534.9, 3449.6, 3673.8, 3962.2, 4194.7], # DE; https://de.statista.com/statistik/daten/studie/14397/umfrage/deutschland-bruttoinlandsprodukt-bip/
    "ES": [1325.6, 1355.6, 1372.2, 1196.3, 1233.2, 1312.8, 1422.4, 1394.5, 1277.1, 1446.6, 1418.9, 1581.2], # ES; https://de.statista.com/statistik/daten/studie/19358/umfrage/bruttoinlandsprodukt-in-spanien/
    "FR": [2685.4, 2811.9, 2856.7, 2439.4, 2472.3, 2594.2, 2792.2, 2729.2, 2645.3, 2958.3, 2780.4, 3031.8], # FR; https://de.statista.com/statistik/daten/studie/14396/umfrage/bruttoinlandsprodukt-in-frankreich/
    "IT": [2088.28,2141.95,2162.57,1836.82,1876.55,1961.10,2092.88,2011.53,1895.94,2156.31,2068.60,2255.50], # IT; https://de.statista.com/statistik/daten/studie/14402/umfrage/bruttoinlandsprodukt-in-italien/
    "AT": [318.7, 323.9, 333.1, 344.3, 357.6, 369.4, 385.3, 397.2, 381, 406.1, 447.7, np.nan] # AT; https://de.statista.com/statistik/daten/studie/14390/umfrage/bruttoinlandsprodukt-in-oesterreich/
}
bipdf = pd.Series(bips)

for i, country in enumerate(countries):
    # print(np.multiply(bsndf[country],bips[country])*0.01)
    ax.plot(heads[1:], bsndf[country]*bips[country]*0.01, lw=1, label=f"{country} (BSN)", linestyle="--")
for country in countries:
    ax.plot(heads[1:], govdf[country]*bips[country]*0.01, lw=1, label=f"{country} (GOV)")

# ax2 = plt.twinx()
# for i, country in enumerate(countries):
#     ax2.plot(heads[1:], bips[country], lw=.75)

ax.legend(loc="upper left")
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.tick_params(axis='x', labelrotation=45)
# ax.set_ylim(ymin=0.05, ymax=.4)
ax.grid(axis="both", alpha=.5)
plt.tight_layout()
# plt.show()
plt.savefig("stat/InvPerBIP2024/InvPerBIP2024.svg")