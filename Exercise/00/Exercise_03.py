"""
3. Cities in Sweden - gender
We continue with the same Excel-file as in task 2, but now you should also read in the sheets
"Kvinnor" and "Män" into two additional DataFrames.
In this task, many operations are similar to all three datasets,
try creating custom made functions to reuse as much code as possible.

  a) Clean your data so that the head looks like this:
  b) Merge the male and female DataFrames vertically and set index to "Kommun". Note that there now should be 580 rows now.
  c) Extract and change column name from the total DataFrame so that the head look like this:
  d) Merge this data with the data in b) so that the head look like this:
  e) Create barplots showing the gender populations of Swedens 10 largest and 10 smallest cities.
  f) Create a pie chart showing the total male and female population in Sweden 2020.
  g) Create a barplot showing the cities with the five largest percentual gender difference in 2020.
  h) Create a barplot showing the top 5 cities with largest populational growth from 2019 to 2020
  i) Feel free to investigate other questions you are interested in using these datasets. ()
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# a) read the data and clean your data
# a) read the data and clean your data
total_population = pd.read_excel("../../Data/komtopp50_2020.xlsx", sheet_name="Totalt", skiprows=6)
women_population = pd.read_excel("../../Data/komtopp50_2020.xlsx", sheet_name="Kvinnor", skiprows=6)
male_population = pd.read_excel("../../Data/komtopp50_2020.xlsx", sheet_name="Män", skiprows=6)

column_dict = {2020: "Rang 2020", 2019: "Rang 2019", "Unnamed: 2": "Kommun",
               "2020.1": "Folkmängd 2020", "2019.1": "Folkmängd 2019", "%": "Förändring"}


# rename and clean
def rename_columns(col_dict, *population):
    [populate.rename(columns=col_dict, inplace=True) for populate in population]


rename_columns(column_dict, total_population, women_population, male_population)

# add new columns
women_population["Kön"] = "Kvinna"
male_population["Kön"] = "Man"

# b) Merge the male and female DataFrames vertically and set index to "Kommun"
women_male = (pd.concat([women_population, male_population])).drop(labels=["Rang 2020", "Rang 2019"], axis=1).set_index("Kommun")


# c) Extract and change column name from the total DataFrame
# dict for change columns name
column_dict2 = {2020: "Rang 2020", 2019: "Rang 2019", "Folkmängd 2020": "Total Pop 2020",
               "Folkmängd 2019": "Total Pop 2019", "Förändring": "Total förändring"}
rename_columns(column_dict2, total_population)

delta_population = total_population.drop(labels=["Rang 2020", "Rang 2019"], axis=1)


# d) Merge this data with the data in b)
merged_kommun = women_male.merge(delta_population, left_on="Kommun", right_on="Kommun")
#print(merged_kommun.info())

# Create barplots showing the gender populations of Swedens 10 largest and 10 smallest cities
largest_10_cities = merged_kommun.sort_values(by="Folkmängd 2020", ascending=False).head(20)
smallest_10_cities = merged_kommun.sort_values(by="Folkmängd 2020", ascending=True).head(20)

fig, ax = plt.subplots(1, 2, dpi=100, figsize=(12,4))
sns.barplot(data=largest_10_cities, x="Folkmängd 2020", y="Kommun", hue="Kön", orient="horizontal", ax=ax[0])
ax[0].set_title("Population in the 10 largest cities")
sns.barplot(data=smallest_10_cities, x="Folkmängd 2020", y="Kommun", hue="Kön", orient="horizontal", ax=ax[1])
ax[1].set_title("Population in the 10 smallest cities")

# f) Create a pie chart showing the total male and female population in Sweden 2020.
female_pop = women_population["Folkmängd 2020"].sum()
male_pop = male_population["Folkmängd 2020"].sum()

fig, ax = plt.subplots(dpi=100)
ax.pie((female_pop, male_pop), labels=("kvinnor", "män"), autopct='%1.1f%%',startangle=90)
ax.axis("equal")

# g) Create a barplot showing the cities with the five largest percentual gender difference in 2020

five_largest_gender_diff = (abs(women_population["Folkmängd 2020"] - male_population["Folkmängd 2020"])
                            /(women_population["Folkmängd 2020"] + male_population["Folkmängd 2020"])).sort_values(ascending=False).head(5)

print("five largest gender diff\n",five_largest_gender_diff)
stad = delta_population.loc[abs((women_population["Folkmängd 2020"] - male_population["Folkmängd 2020"])
                            /(women_population["Folkmängd 2020"] + male_population["Folkmängd 2020"])).isin((five_largest_gender_diff))]#.sort_values(by="Total förändring", ascending=False)

fig, ax = plt.subplots(dpi=100)
ax = sns.barplot(data=stad, x="Kommun", y="Total förändring")
ax.set_title("Five largest percentual gender difference in 2020")

# h) Create a barplot showing the top 5 cities with largest populational growth from 2019 to 2020
largest_pop_growth = delta_population["Total förändring"].sort_values(ascending=False).head(5)
kommun = delta_population.loc[delta_population["Total förändring"].isin(largest_pop_growth)]\
    .sort_values(by="Total förändring", ascending=False)

fig, ax = plt.subplots(dpi=100)
ax = sns.barplot(data=kommun, x='Kommun', y='Total förändring')
ax.set_title("Top 5 cities with largest populational growth")
plt.show()

# i) Feel free to investigate other questions you are interested in using these datasets.

