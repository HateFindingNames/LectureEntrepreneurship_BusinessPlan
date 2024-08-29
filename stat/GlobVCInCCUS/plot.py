import matplotlib.pyplot as plt
import pandas as pd
import os

file = "\\statistic_id1411549_global-ccus-startup-vc-investment-2018-2022-by-quarter.csv"

heads = ["Periode", "Inv"]
with open(os.path.dirname(__file__)+file) as f:
    invdf = pd.read_csv(f, names=heads)


fig, ax = plt.subplots(1,1,figsize=(10,5))

xlabel = ""
ylabel = "VCF in Mrd. USD"
title = "Globale Venture Capital Finanzierung (VCF) in CCUS Start-Ups in Milliarden USD"
ax.bar(invdf["Periode"], invdf["Inv"])
ax.tick_params(axis='x', labelrotation=45)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.grid(axis="y", alpha=.5)
plt.tight_layout()
# plt.show()
plt.savefig("stat\\GlobVCInCCUS\\ccus-startup-vc-investment.svg")