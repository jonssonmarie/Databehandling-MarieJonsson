"""
2. Cities in Sweden - real dataset
Go into this page, scroll down and download the Excel file containing Swedish population dataset from SCB.

a) Read in the tab "Totalt" into a DataFrame and start exploring the data with some simple explorations such as
df.head()
df.info()
df.describe()
Feel free to do more explorations.

b) Clean your data so that the head looks like this:

Rang 2020	Rang 2019	Kommun	Folkmängd 2020	Folkmängd 2019	Förändring
0	83	    84	        Ale	        31868	       31402	      1.48398
1	64	    64	        Alingsås    41602	       41420	      0.439401
2	123	    123	        Alvesta	    20224	        20134	      0.447005
3	255	    255	        Aneby	    6821	        6848	      -0.394276
4	169	    167	        Arboga	    14039	        14087	      -0.34074

c) Sort the cities by population from largest to smallest.
d) Filter out the five smallest cities.
e) Use the DataFrame to calculate Sweden's population in 2019 and 2020.
f) Plot a bar chart for the five largest cities and the five smallest cities.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# a) read the data
total_pop_sweden = pd.read_excel("../Data/komtopp50_2020.xlsx", sheet_name="Totalt", skiprows=6)
total_pop_sweden.head()
total_pop_sweden.info()
#print(total_pop_sweden.describe())

# b) rename and clean
total_pop_sweden.rename(columns={2020: "Rang 2020", 2019: "Rang 2019", "Unnamed: 2": "Kommun",
                                "2020.1": "Folkmängd 2020", "2019.1": "Folkmängd 2019", "%": "Förändring"},
                                inplace=True)
#print(total_pop_sweden.head(5))

# c)
pop_sorted_descending = total_pop_sweden.sort_values(by="Folkmängd 2020", ascending=False)
#print(pop_sorted)

# d)
pop_sorted_ascending = total_pop_sweden.sort_values(by="Folkmängd 2020", ascending=True)
pop_five_smallest = pop_sorted_ascending.head(5)
print(pop_five_smallest)
# alternativt så här
# print(pop_sorted_ascending.iloc[:5])

# e) calculate Sweden's population in 2019 and 2020
population_2020 = total_pop_sweden["Folkmängd 2020"].sum()   # dataFrame.sum()
population_2019 = total_pop_sweden["Folkmängd 2019"].sum()
print(f"population 2020: {population_2020}")
print(f"population 2019: {population_2019}")

# f) the five largest cities and the five smallest cities
fig, ax = plt.subplots(1, 2, dpi=100 ,figsize=(12,4))

sns.barplot(data=pop_five_smallest, x="Kommun", y="Folkmängd 2020", ax=ax[0])
ax[0].set_title("Folkmängd 5 minsta kommunerna")
sns.barplot(data=pop_sorted_descending.head(5), x="Kommun", y="Folkmängd 2020", ax=ax[1])
ax[1].set_title("Folkmängd 5 största kommunerna")
plt.show()
