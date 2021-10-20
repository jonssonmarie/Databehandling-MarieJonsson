"""
1. Find missing values
  a) Read in the file "student-mat-missing-data.csv" into a Pandas DataFrame
  b) Do some initial explorations with the methods to get an understanding of the dataset:
     head(), info(), describe(), value_counts(), unique(), columns
  c) Create a function that takes in a DataFrame as input parameter and plots a barplot with the columns
     that have missing values. Put this function into a file called data_utils.py.
     When you come across more useful functions, you can store them in your data_utils module.
  d) Now import your function from the module data_utils and use it to visualize NaNs in your dataset.
  e) Find all rows where the freetime is NaN.
  f) Find all rows where the freetime or the age is NaN.
  g) You will notice that some rows have several NaNs. Now compute the proportion that these rows
    constitute of the whole dataset.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# a) read file
path = r"../../Data/student-mat-missing-data.csv"
student = pd.read_csv(path, sep=",")

# b) initial explorations head(), info(), describe(), value_counts(), unique(), columns
# print("head:\n", student.head(), "\n")
print("info:\n", student.info(), "\n")
"""print("describe:\n", student.describe(), "\n")
print("value_counts:\n", student["reason"].value_counts(), "\n")
print("unique school:\n", student['school'].unique(), "\n")
print("unique school:\n", student['sex'].unique(), "\n")
print("unique school:\n", student['studytime'].unique(), "\n")
print("columns:\n", student.columns, "\n")"""

# c) see data_utils.py
"""c) Create a function that takes in a DataFrame as input parameter and plots a barplot with the columns
     that have missing values. Put this function into a file called data_utils.py.
     When you come across more useful functions, you can store them in your data_utils module."""


def plot_columns(df):
    num_missings = []
    col_w_nan = ["age","address","famrel", "freetime", "goout", "health", "absences"]

    for i in col_w_nan:
        num_missing = (df[i].isnull() == True).sum()
        num = df[i].isnull()
        print("num_missing", i, num_missing)
        num_missings.append(num_missing)
        df = df[num]

    # FEL KOLLA MED Kokchun
    fig, ax = plt.subplots(dpi=100)
    ax = sns.barplot(data=num_missings, x=None, y=None)
    ax.set_title("jadu")
    plt.show()


plot_columns(student)


# d) import your function from the module data_utils and use it to visualize NaNs in your dataset

# e) Find all rows where the freetime is NaN.
row_w_nan = student[student["freetime"].isna() == True]
print("freetime with nan\n", row_w_nan["freetime"].index)

# f) Find all rows where the freetime or the age is NaN.
row_w_nans = student[student["age"].isna() == True]
row_2col_nans = pd.concat([row_w_nan["freetime"], row_w_nans["age"]], axis=1)


print("The rows with NaN",row_2col_nans[["freetime", "age"]].index)
#print(student.isnull().sum())


# g) You will notice that some rows have several NaNs. Now compute the proportion that these rows
#   constitute of the whole dataset.

num_missings = []
col_w_nan = ["age","address","famrel", "freetime", "goout", "health", "absences"]

for i in col_w_nan:
    num_missing = (student[i].isnull() == True).sum()
    num = student[i].isnull()
    print("num_missing", i, num_missing)
    num_missings.append(num_missing)
    df = student[num]

print(sum(num_missings)/(student.shape[0]*33))
print((num_missings[0] + num_missings[3])/(student.shape[0]*33))  # får det inte till 0.0127 of the dataset


num_nan_freetime = row_w_nan.index.value_counts().sum()
num_nana_age = row_w_nans.index.value_counts().sum()
print(" num nan  ",num_nan_freetime, num_nana_age)

