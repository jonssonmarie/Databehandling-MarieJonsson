"""
c) Create a function that takes in a DataFrame as input parameter and plots a barplot with the columns
     that have missing values. Put this function into a file called data_utils.py.
     When you come across more useful functions, you can store them in your data_utils module.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def plot_columns(df):
    df_nans = df[df.columns[df.isna().any() == True]]
    sns.barplot(data=df_nans)
    plt.show()