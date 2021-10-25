"""
Merging datasets
"""
# setup
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(16).reshape(4,4), columns=list("ABCD"))
df2 = pd.DataFrame(np.zeros((3,4)), columns=list("ABCD"))
#print(df2)

""" 
Concat 
  - Concatenates along a particular axis
  - set logic
"""
df3 = pd.concat([df1,df2], axis=0).reset_index(drop=True)  # df1.shape(4,4) df2.shape (3,4))  så lägger till NaN
df4 = pd.concat([df1,df2], axis=1, join="inner") # Intersection, inner klipper iom detta den sista raden i df1
df5 = pd.concat([df1,df2], axis=1, join="outer") #  Union , inner klipper iom detta inte den sista raden i df1 -> Unit A eller Unit B
"""print(df3)
print(df4)
print(df5)"""

"""
Merge
- different join operations similar to relational datasets as SQL
"""

left = pd.DataFrame(
    {
        "key": ["K0", "K0", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

df7 = pd.merge(left,right, on="key", indicator=True)
#print(df7)

df8 = left.merge(right, on="key", how="outer", indicator=True)
#print(df8)

link = "https://en.wikipedia.org/wiki/List_of_potentially_habitable_exoplanets"
tables= pd.read_html(link)  # tar alla tabeller och lägger dem i en lista. OM hemsidan är bra kodad
exo_planets = tables[0].head()
print(exo_planets.head())

link2 = "https://en.wikipedia.org/wiki/FIFA_World_Cup"
print(exo_planets.Object.unique())  # exo_planets["Obejct"].unique() fungerar också
fifa_tables = pd.read_html(link2, match="Hosts")[0]