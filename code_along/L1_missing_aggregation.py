"""
Missing data and aggregations
 - in real world, there will be missing data and or unwanted disturbance data
   Shit in, shit out

Setup:
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)  # np random kan skapa random arrayer
n = 10
# create dummy data
random_matrix = np.random.randint(1, 10, [n, n])  # ger en matris 5x5 är en 2D array i Python
index = np.random.choice(random_matrix.size, 10, replace=False)
#print(index)
#print(random_matrix)
#print(random_matrix.size)
random_matrix = random_matrix * 1.0
random_matrix.ravel()[index] = None  # måste vara float in därav type-omvandlingen raden ovan
#print(random_matrix)

scores = pd.DataFrame(random_matrix, index=[f"Player {i}" for i in range(1, n+1)],
                      columns=[f"Round {i}" for i in range(1, n+1)])
#print(scores)


""" 
Missing value Methods:
  - isnull() - returns True if null
  - notnull() - returns True if not null
  - dropna() - drops an axis if any null, use : how{‘any’, ‘all’}, default ‘any’ for drop if ALL are NaN
  - fillna() - fills the null values with certain value
"""

# how to treat NaNs?
# depends on the situations
# many times need to talk to domain experts

scores.fillna(0)  # in this case - may be reasonable to give 0 scores for missing value
# scores.fillna("Miss") sätter "Miss" på alla NaN

""" 
Missing value strategy
Strategy depends on :
   - dataset size 
   - valuable inforamtion (some rows, some columns)
   - percentage missing values
   - domain knowledge
   - missing values can impact:
        - data visualization
        - arithmetic computations
        - summary statistics
        - machine learning algorithms
"""

titanic = sns.load_dataset("titanic")
#print(titanic.isnull().sum())
# focus on age in this example

sns.histplot(data=titanic, x="age", kde=True, hue="sex", multiple="dodge")  # “stack”, "dodge", “fill”, "layer"})
sns.set_theme()
plt.show()

"""
talked to a titanic historian (not a real historian)
this dude says: use median age of corresponding gender to fill in ages
"""

print(f"Number of males: {np.sum(titanic['sex'] == 'male')}")
print(f"Number of females: {np.sum(titanic['sex'] == 'female')}")

median_male_age = titanic.loc[titanic['sex'] == 'male','age'].median()
median_female_age = titanic.loc[titanic['sex'] == 'female','age'].median()

print("median_male_age",median_male_age)
print("median_female_age", median_female_age)

titanic.loc[titanic['sex'] == 'male','age'] = titanic.loc[titanic['sex'] == 'male','age'].fillna(median_male_age)
titanic.loc[titanic['sex'] == 'female','age'] = titanic.loc[titanic['sex'] == 'female','age'].fillna(median_female_age)
print("Num of people with age 29",titanic.loc[titanic['age'] == 29, 'sex'].value_counts())
print("Num of people with age 27",titanic.loc[titanic['age'] == 27, 'sex'].value_counts())

sns.histplot(data=titanic, x="age", kde=True, hue="sex", multiple="stack", bins=50) # “stack”, "dodge", “fill”, "layer"})
sns.set_theme()
#plt.show()

# groupby
mean_value = titanic.groupby("sex").mean()
print(mean_value)
median_value = titanic.groupby("sex").median()
print(median_value)
mean_value_2col = titanic.groupby("sex").mean()[["survived", "age"]]
print("mean",mean_value_2col)

