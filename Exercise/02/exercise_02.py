"""
2. Denmark demographic data
Go to the Danish-language wikipedia page Danmarks demografi.
  a) Read in the table under "Demografiske data" into a DataFrame
  b) Clean the data and draw a graph of population against year from 1769-2020.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

den_demografi_link = "https://da.wikipedia.org/wiki/Danmarks_demografi"
den_demografi = pd.read_html(den_demografi_link, match="Befolkning", thousands=".", header=None)[0]\
                    .rename(columns={"Befolkning pr. 1. januar": "Befolkning", "År": "År", "År.1": "År", "Befolkning pr. 1. januar.1": "Befolkning"})


den_demografi_part1 = den_demografi.iloc[:, :2]
den_demografi_part1["Befolkning"] = den_demografi_part1["Befolkning"].str.replace("\[5\]","")\
                                        .str.replace(".","").astype(int)
den_demografi_part1["År"] = den_demografi_part1["År"].astype(int)


den_demografi_part2 = den_demografi.iloc[:, 2:].dropna()
den_demografi_part2["År"] = den_demografi_part2["År"].astype(int)
den_demografi_part2["Befolkning"] = den_demografi_part2["Befolkning"].str.replace(",","").astype(int)


den_demografi_clean = pd.concat([den_demografi_part1, den_demografi_part2], axis=0, join="outer").reset_index()
print(den_demografi_clean)

fig , ax = plt.subplots(dpi=100, figsize=(10,8))
sns.lineplot(data=den_demografi_clean, x="År", y="Befolkning").set(title="Danmarks befolkningsförändring 800 -2020")
plt.show()
