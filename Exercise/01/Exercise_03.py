"""
3. Clean freetime column
Now there are missing data on freetime that needs to be filled.

Try yourself and find reasonable approaches for how you would fill those missing data.
Document what you have tried and different findings
Combine suitable visualizations with pandas methods
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px


# a) read file
path = r"../../Data/student-mat-missing-data.csv"
student = pd.read_csv(path, sep=",")

# freetime - free time after school (numeric: from 1 - very low to 5 - very high)
# since freetime use int, I rounded down or up

freetime_missingdata = student[student["freetime"].isna() == True]["freetime"]  # tar fram alla NaN i freetime
freetime_mean1 = student[student["freetime"].isna() == False]  # tar fram alla utan NaN i freetime
freetime_mean = freetime_mean1["freetime"].mean().astype(int)  # räknar ut mean för freetime och omvandlar till int

freetime_mean_ages = (freetime_mean1.groupby("age")).mean()["freetime"].mean().round().astype(int)
# samlar ihop alla age-data, tar medel sedan avrundar och sedan till int
#print("freetime_missingdata\n",freetime_missingdata)  # print av alla NaN
#print("freetime_mean1\n",freetime_mean1)
#print("freetime_mean\n",freetime_mean)
#print("freetime_mean_ages\n", freetime_mean_ages)

# plot med alla freetime som medelvärde
student.loc[student["freetime"] == 'freetime'] = student.loc[student["freetime"] == 'freetime'].fillna(freetime_mean)
#print("Any NaN in Freetime:\n", student[student["freetime"].isna() == True])
fig, ax = plt.subplots(dpi=100)
sns.barplot(data=student, x="age", y="freetime").set(title="Freetime filled 3")  #, hue="age"

# tar fram alla åldras medelvärde på freetime, sedan tar jag medelvärde på dessa igen
student.loc[student["freetime"] == 'freetime'] = student.loc[student["freetime"] == 'freetime'].fillna(freetime_mean_ages)
#print("Any NaN in Freetime:\n", student[student["freetime"].isna() == True])
# inga NaN kvar

fig, ax = plt.subplots(dpi=100)
sns.barplot(data=student, x="age", y="freetime").set(title="Freetime filled 4")  # , hue='age'

# testar med bara age 16-19 och fyller i freetime med medelvärdet av dessa
ages16to19 = student[(student.age >= 16.0) & (student.age < 19.0)]
freetime_mean1 = ages16to19[ages16to19["freetime"].isna() == False]
freetime_mean = freetime_mean1["freetime"].mean().astype(int)
freetime_mean_ages2 = (freetime_mean1.groupby("age")).mean()["freetime"].mean().round().astype(int)
ages16to19.loc[ages16to19["freetime"] == 'freetime'] = ages16to19.loc[ages16to19["freetime"] == 'freetime'].fillna(freetime_mean_ages2)
print("freetime_mean_ages2", freetime_mean_ages2)

fig, ax = plt.subplots(dpi=100)
sns.barplot(data=ages16to19, x="age", y="freetime").set(title="Freetime filled for mean age 16-19 (3)")
plt.show()