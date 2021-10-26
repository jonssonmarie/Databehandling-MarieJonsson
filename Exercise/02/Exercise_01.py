"""
1. Swedish demographic data
Go to Swedish-language wikipedia page Sveriges demografi.
a) Read in the table under "Befolkningsstatistik sedan 1900" into a DataFrame
b) Choose to do some EDA (exploratory data analysis) on this dataset. And draw some relevant graphs.
c) Now we want to go backwards in time (before 1900) to see how population has changed in Sweden.
   Read in the table under history and keep the data of "Folkmängd" from 1570-1865.

År	Folkmängd
1570	900000
1650	1225000
1700	1485000
1720	1350000
1755	1878000
1815	2465000
1865	4099000
d) Now concatenate this with the table from 1900 so that you have population data from 1570 to 2020.
   Note that you may need to clean the data in order for it to fit properly.
   Also you may be able to do this in several ways.
e) Draw a graph of population data from 1570-2020.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# a)
swe_demografi_link = "https://sv.wikipedia.org/wiki/Sveriges_demografi"

swe_demograf = pd.read_html(swe_demografi_link, match="Födda", thousands=" ")[0].rename(columns={"Unnamed: 0" :"År"})

# Födda(int), Döda(int), Nativiteten(float) per 1000
# b)
df_col = swe_demograf[["År","Födda", "Döda"]]
fig, ax = plt.subplots( dpi=100, figsize=(13, 9))
sns.lineplot(data=df_col)


# c)
swe_demograf_1570to1865 = pd.read_html(swe_demografi_link, match="Promille",thousands="\xa0", skiprows=0)[0].iloc[:7, :2]\
    .rename(columns={"Vid utgången av år": "År"}).droplevel(0, axis=1)

swe_demograf_1570to1865["Folkmängd"] = swe_demograf_1570to1865["Folkmängd"].astype(int)
swe_demograf_1570to1865["År"] = swe_demograf_1570to1865["År"].astype(int)


# d) Now concatenate this with the table from 1900 so that you have population data from 1570 to 2020.
swe_demograf["Folkmängd"] = swe_demograf["Folkmängd"].astype(int)
swe_demograf["År"] = swe_demograf["År"].astype(int)

swe_demograf = swe_demograf.iloc[:, :2]

swe_demografi_1570to2020 = pd.concat([swe_demograf_1570to1865, swe_demograf], axis=0, join="outer").reset_index(drop=True)
print(swe_demografi_1570to2020.info())

# e) Plot
fig, ax = plt.subplots(dpi=100, figsize=(13, 9))
sns.lineplot(data=swe_demografi_1570to2020, x="År", y="Folkmängd", color="r").set(title= "1570 - 2020")
plt.show()
