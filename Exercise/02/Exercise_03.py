"""
3. Norwegian demographic data
Go to Swedish-language wikipedia page Norges demografi.
a) Read in the table under "Befolkningsstatistik sedan 1900" into a DataFrame
b) You see some missing data in column "Total fertilitet".
   Go to the English page and read in the data from "Vital statistics since 1900".
c) Pick out the fertility column from b) dataset, merge it into a)
   dataset and clean the data so that you only have columns "År", "Folkmängd", "Fertilitet".
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# links
nor_demografi_link= "https://sv.wikipedia.org/wiki/Norges_demografi"
nor_fertility_link = "https://en.wikipedia.org/wiki/Demographics_of_Norway"

# read tables
nor_demografi = pd.read_html(nor_demografi_link, match="Födda", thousands=" ")[0]\
    .rename(columns={"Unnamed: 0": "År", "Befolkning i tusentals (x 1000)": "Folkmängd"}).iloc[:, [0, 1, 8]]

nor_fertility = pd.read_html(nor_fertility_link, match="Average population")[0]\
    .rename(columns={"Unnamed: 0": "År","Average population": "Folkmängd", "Total fertility rates[fn 1][5][7]": "Fertility"}).iloc[:,[0, 1, 8]]

# change type
nor_demografi["Folkmängd"] = np.multiply(nor_demografi["Folkmängd"].astype(int), 1000)

#  Df för Norsk demografi:  År, Folkmängd, Fertilitet
nor_demografi_fertility = (nor_demografi.merge(nor_fertility.iloc[:,[0,2]], how="outer", on="År")).iloc[:, [0,1,3]]
nor_demografi_fertility["Folkmängd"] =nor_fertility["Folkmängd"]
nor_demografi_fertility.drop(nor_demografi_fertility.tail(1).index, inplace=True)  # drop last row (2021) with nan

# prints
#print(nor_demografi)
#print(nor_fertility.info())
print(nor_demografi_fertility.tail())

# plot bara för att öva
fig, ax = plt.subplots(dpi=100, figsize=(10,8))
sns.lineplot(data=nor_demografi_fertility, x="Folkmängd", y="År")
plt.show()
fig, ax = plt.subplots(dpi=100, figsize=(10,8))
sns.lineplot(data=nor_demografi_fertility, x="Fertility", y="År")

plt.show()
