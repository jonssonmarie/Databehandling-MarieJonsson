import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"""
Intro till Pandas
- series object
DataFrame object
"""

data = dict(AI=25, NET=30, APP=27, Java=23)
series = pd.Series(data=data)
#print(series)

"""
OUTPUT: 
AI      25
NET     30
APP     27
Java    23 
dtype: int64   HÅRDTYPAT vilket Python snabbare, VIKTIGT i Pandas och Numpy
int64 - en integer med 64 bitar


om string i data data = dict(AI=25, NET=30, APP=27, Java="23")
ger: dtype: object men även för andra datatyper tex bool, men 30.0 ger float64
AI      25
NET     30
APP     27
Java    23
dtype: object
"""
# extracting values
#print(f"series[0]: {series[0]}")
#print(f"series[-1]: {series[-1]}")

# extracting keys
#print(f"series[-2]: {series.keys()[-2]}")

# DataFrame
df = pd.DataFrame(series, columns=("Number Students",))  # behöver en tuple av två så därför ,
#print(df)

languages = pd.Series(dict(AI="Python", NET="C#", APP="Kotlin", Java="JAVA"))
df = pd.DataFrame({"Students": series, "Languages":languages})
#print(df)
#print(df.index)
#print(df.columns)  # når titlarna på kolumnerna

#print(df.Students)  # gets a Series with a attribute- approach
#print(df["Students"])  # gets a Series with dictionary-keys approach - more stable than attribute-approach above (__getitem__())

# multiple columns
#print(df[["Language", "Students"]])  # bytt ordning och lagt till sublisto

# wants to get all rows > 24 students

#print(df["Students"] > 24)  # __gt__()
"""
AI       True
NET      True
APP      True
Java    False
Name: Students, dtype: bool
"""
large_groups = df[df["Students"] > 24]
#print(df[df["Students"] > 24])  # picked out all rows that are True
"""
     Students Languages
AI         25    Python
NET        30        C#
APP        27    Kotlin
"""

sns.barplot(data= large_groups, x=large_groups.index, y="Students")
plt.title("Antal studenter i olika program")
#plt.show() # behövs för seaborn i py script      can also use seaborns methods for this

# read Excel

calories = pd.read_excel("../Data/calories.xlsx")
# print(calories)  # [2225 rows x 5 columns]
print(calories.head(3))  # ger tre första raderna (0-2) utöver columnnamn
#print(calories.iloc[3:8]) # iloc ger 3 till 8-1
#print(calories.info())  # ger bla lagringsstorleken, vilket object, columns namn
#print(calories.describe())  # gives statistics on dataframe
#print(calories["FoodCategory"].unique())   # Uniques are returned in order of appearance. This does NOT sort.

# Data cleaning
"""
- convert string to int
- change column names
- separate liquids and solids
"""

calories = calories.rename(dict(Cals_per100grams="Calories", per100grams="per100", KJ_per100grams="kJ"), axis="columns")
print("\n",calories.head(1))

calories["Calories"] = calories["Calories"].str[:-3].astype(int)
calories["FoodItem"] = calories["FoodItem"].str[:-3].astype(str)
print("\n",calories.head())

solids = calories[calories["per100"] == "100g"]
liquids = calories[calories["per100"] == "100ml"]

# find top 5 categories with highest calories
solids_sorted = solids.sort_values(by="Calories", ascending=False).head()
solids_top5 = solids_sorted.iloc[:5]
print("solids_top5",solids_top5)

fig, ax = plt.subplots(1,2, dpi=100, figsize=(12,4))
sns.barplot(data=solids_top5, x="FoodItem", y="Calories", ax=ax[0])
sns.barplot(data=solids_top5, x="FoodItem", y="Calories", ax=ax[1])
#plt.show()