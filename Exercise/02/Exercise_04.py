"""
4. Merge Sweden-Norway
Create a population graph and a fertility graph showing Sweden and Norway.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Exercise_03 import fertility
#from Exercise_01 import population_data

# Links
swe_demografi_link = "https://sv.wikipedia.org/wiki/Sveriges_demografi"
nor_demografi_link= "https://sv.wikipedia.org/wiki/Norges_demografi"

# read tables
swe_demograf = pd.read_html(swe_demografi_link, match="Födda", thousands=" ", decimal=",")[0]\
                .rename(columns={"Unnamed: 0" :"År", "Total fertilitet": "Fertilitet"}).iloc[:,[0, 1, 8]]

nor_demografi = pd.read_html(nor_demografi_link, match="Födda", thousands=" ")[0]\
    .rename(columns={"Unnamed: 0": "År", "Befolkning i tusentals (x 1000)": "Folkmängd"}).iloc[:, [0, 1, 8]]

nor_demograf = fertility(nor_demografi)

# plot
fig, ax = plt.subplots(1,2, dpi=100, figsize=(15,10))
sns.lineplot(data=swe_demograf, x="År", y="Fertilitet", ax=ax[1]).set(title="Swedens fertility")
sns.lineplot(data=nor_demograf, x="År", y="Fertilitet", ax=ax[0]).set(title="Norways fertility")
plt.show()
