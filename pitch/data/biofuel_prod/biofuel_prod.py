# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Apply the default theme
# sns.set_theme("dark")

# dat = "./produktion-von-biokraftstoffen-in-deutschland-und-eu-bis-2023.csv"
dat = "pitch\\data\\biofuel_prod\\produktion-von-biokraftstoffen-in-deutschland-und-EU-und-WW-bis-2023.csv"

data = pd.read_csv(dat, sep=",")

xlabel = "Jahr"
ylabel = "Produktion in 1000 Barrel Öläquivalent pro Tag"
title = "Biokraftstoffproduktion in Deutschland, EU und Weltweit"

# Set the color palette using seaborn
# palette = sns.color_palette("dark", len(data.columns) - 1)  # 'husl' is an example palette

# data["EU"] = (data["EU"] / data.at[29, "EU"])
# data["De"] = (data["De"] / data.at[29, "De"])
# data["WW"] = (data["WW"] / data.at[29, "WW"])
# print(data.at[29 "EU"])
# print(data)

ax = data.plot.bar(x="Jahr", figsize=(12, 6), xlabel="", ylabel=ylabel, title=title, rot=45, stacked=True, color=["green", "limegreen", "lightblue"])
# plt.grid()

# Schwellenwert definieren
threshold = 5

# Annotate the bars with their respective values
# for container in ax.containers:
#     labels = [int(val) if val > threshold else '' for val in container.datavalues]
#     ax.bar_label(container, labels=labels, label_type='edge')

# plt.show()
plt.savefig("pitch\\data\\biofuel_prod\\biofuel_prod.svg")
plt.savefig("pitch\\data\\biofuel_prod\\biofuel_prod.png")