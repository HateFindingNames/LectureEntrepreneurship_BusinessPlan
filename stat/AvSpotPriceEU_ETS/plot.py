import matplotlib.pyplot as plt
import pandas as pd
import os

file = "\\AvSpotpriceEU_ETS.csv"

heads = ["Jahr", "Preis"]
with open(os.path.dirname(__file__)+file) as f:
    invdf = pd.read_csv(f, names=heads)


fig, ax = plt.subplots(1,1,figsize=(10,5))

xlabel = ""
ylabel = "EUR pro Tonne"
title = "Gemittelte Preise der EU-ETS am Spotmlarkt von 2010 bis 2024 in EUR pro Tonne CO2"
ax.plot(invdf["Jahr"], invdf["Preis"])
ax.tick_params(axis='x', labelrotation=45)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.grid(axis="y", alpha=.5)
plt.tight_layout()
# plt.show()
plt.savefig("stat\\AvSpotPriceEU_ETS\\AvSpotPriceEU_ETS.svg")