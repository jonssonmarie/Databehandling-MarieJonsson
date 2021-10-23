"""
2. Clean the data
  a) As you have conversed with a domain expert you both agree that there are too many missing data
     to fill in and the proportion is small enough to be safe to just remove.
     Now remove these rows and use your missing-value utility function visualize the remaining NaNs.
  b) The domain expert has told you that you have to fill in the missing age values.
     Start with visualising the age distribution in the dataset using a histogram.
  c) Check which columns there are in the dataset to see what can be utilised in determining the age.
  d) The column higher seems interesting. Let's see which unique values it can have.
  e) Let's see if we can see some connection between age distribution and higher. Make 3 subplots of age histograms:

Plot 1: same as b)
Plot 2: age distribution when higher is yes
Plot 3: age distribution when higher is no
  f) That was hard to find a connection. When reading dataset source we find alcohol consumption,
     maybe there is some connection between age and alcohol consumption.
     Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
     Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
     Start with creating a new column called Alcohol, which is a sum of Dalc and Walc columns
  g) Make a barchart for alcohol consumption vs age.
  h) We see that older students tend to drink more, but notice how few 20-22 year-old students we have in the dataset.
     We can definitely exclude them when computing the missing values.
     However there are also few 19 year-old students in the dataset,
     say for simplicity that we can exclude them as well. This leaves:

alcohol level >= 4 -> 16, 17 or 18 years old -> take median to simplify
alcohol level < 4 -> 15 years old
Fill these in and visualize missing values.

Note: could make more stringent by computing percentages based on the distribution
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from data_utils import plot_columns

# a) read file
path = r"../../Data/student-mat-missing-data.csv"
student = pd.read_csv(path, sep=",")

# print("head:\n", student.head(), "\n")
"""
print("info:\n", student.info(), "\n")
print("describe:\n", student.describe(), "\n")
print("value_counts:\n", student["reason"].value_counts(), "\n")
print("unique school:\n", student['school'].unique(), "\n")
print("unique school:\n", student['sex'].unique(), "\n")
print("unique school:\n", student['studytime'].unique(), "\n")
print("columns:\n", student.columns, "\n")
"""

# a)
# dropped rows in columns in subset with NaN
drop_rows = student.dropna(axis=0, subset=["address", "famrel", "goout", "health", "absences"])
#print(drop_rows)

plot_columns(drop_rows)


# b)
fig, ax = plt.subplots(1, 3, dpi=100, figsize=(15, 8))
sns.histplot(data=drop_rows, x="age", ax=ax[0]).set_title("Age distribution")
# strax innan 15 tom strax efter 17 är störst i grupperingen

#c )
# higher verkar vara intressant efter att ha kollat data

"""
Attribute Information:

# Attributes for both student-mat.csv (Math course) and student-por.csv (Portuguese language course) datasets:
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)

# these grades are related with the course subject, Math or Portuguese:
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)
"""

# d)
# yes /no are the values in column higher
# higher - wants to take higher education

# e) Let's see if we can see some connection between age distribution and higher.
higher_yes = drop_rows[drop_rows["higher"] == "yes"]
sns.histplot(data=higher_yes, x="age", ax=ax[1]).set_title("Higher = yes")

higher_no = drop_rows[drop_rows["higher"] == "no"]
sns.histplot(data=higher_no, x="age", ax=ax[2]).set(title="Higher = no")
#plt.show()

# f) Start with creating a new column called Alcohol, which is a sum of Dalc and Walc columns
drop_rows["Alcohol"] = drop_rows["Dalc"] + drop_rows["Walc"]   # drop_rows.loc[: ,['Dalc', 'Walc']].sum(axis=1)

# g) Make a barchart for alcohol consumption vs age.
sns.barplot(data=drop_rows, x="age", y="Alcohol").set(title="alcohol consumption vs age")
#plt.show()

#  h) We see that older students tend to drink more, but notice how few 20-22 year-old students we have in the dataset.
"""
We can definitely exclude them when computing the missing values.
However there are also few 19 year-old students in the dataset,
say for simplicity that we can exclude them as well. This leaves:
 
alcohol level >= 4 -> 16, 17 or 18 years old -> take median to simplify
alcohol level < 4 -> 15 years old
Fill these in and visualize missing values. HITTAR inga NaN

Note: could make more stringent by computing percentages based on the distribution
FATTAR INTE OVANSTÅENDE Fråga Joakim eller Kokchun
KOlla även varning SettingWithCopyWarning: 
"""

age_16to18 = drop_rows[(drop_rows["age"] == drop_rows["age"].median()) & (drop_rows.Alcohol >= 4)]
#drop_rows[(drop_rows.age >= 16.0) & (drop_rows.age < 19.0) & (drop_rows.Alcohol >= 4)]
age_16to18_mean2 = age_16to18[age_16to18["age"].isna() == True].count()

age_16to18_mean = age_16to18.groupby("age").mean()["Alcohol"]

print(age_16to18_mean)
age_15 = drop_rows[(drop_rows["age"] == 15.0) & (drop_rows["Alcohol"] < 4)]
#missing_age15 = age_15[age_15["age"].isna() == True]

fig, ax = plt.subplots(1, 2, dpi=100, figsize=(12,6))
sns.barplot(data=age_16to18, x="age", y="Alcohol", ax=ax[0]).set(title="Alcohol level in ages 16 to 18")
sns.barplot(data=age_15, x="age", y="Alcohol", ax=ax[1]).set(title="Alcohol level in age 15")
plt.show()
