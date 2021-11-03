"""
uppgift 4
länkar:
https://covid19.who.int/table
https://www.ecdc.europa.eu/en/publications-data/data-national-14-day-notification-rate-covid-19
"""

import pandas as pd
import numpy as np
from initial_analyse import analyse
from many_plots import bar_plot

# paths to excel files
who_path = r"../Data/WHO COVID-19 global table data November 1st 2021 at 5.02.45 PM.csv"
ecdc_vaccine_path = r"../Data/Data on COVID-19 vaccination in the EUEEA.csv"

# read excel files
covid_cases_who = pd.read_csv(who_path).reset_index()\
    .rename(columns={"index": "Nation",
            "Cases - cumulative total per 100000 population": "Covid cases - cumulative total per 100000 population"})

vaccine_ecdc = pd.read_csv(ecdc_vaccine_path).iloc[1:, :]

# call on initial_analyse.py
analyse(covid_cases_who)
analyse(vaccine_ecdc)

# List with all countries
country_list = vaccine_ecdc["ReportingCountry"].unique()


def sum_per_column(names, df):
    """ calculate sum from a columns for keys and save to a dataframe
    :param names: str
    :param df: dataFrame object
    :return: dataFrame object
    """
    dos1_dos2 = []
    for name in names:
        dos1 = np.sum(df[(df["Region"] == name) & (df["TargetGroup"] == "ALL")]["FirstDose"])
        dos2 = np.sum(df[(df["Region"] == name) & (df["TargetGroup"] == "ALL")]["SecondDose"])
        pop_region = (df[df["ReportingCountry"] == name]["Population"]).unique()[0]
        summery = [name, pop_region, dos1, dos2]
        dos1_dos2.append(summery)
    all_dos = pd.DataFrame(dos1_dos2, columns=("ReportingCountry", "Population", "FirstDose", "SecondDose"))
    return all_dos


ecdc_vaccine_cases = vaccine_ecdc[["YearWeekISO", "FirstDose", "SecondDose", "Region", "ReportingCountry",
                                 "TargetGroup", "Population"]]
ecdc_vaccine = sum_per_column(country_list, ecdc_vaccine_cases)


# limit data for WHO-cases and drop first row
who_cases = covid_cases_who[["Nation", "WHO Region", "Covid cases - cumulative total per 100000 population",
                             "Deaths - cumulative total per 100000 population"]].iloc[1:, :].dropna()

# split data for cumulative per 100000 population for easier plots
who_cases_below = who_cases[(who_cases["Covid cases - cumulative total per 100000 population"] < 10000)
                            & (who_cases["Covid cases - cumulative total per 100000 population"] > 5000)]

who_cases_above = who_cases[(who_cases["Covid cases - cumulative total per 100000 population"] >= 10000)]
who_cases_below_5000 = who_cases[(who_cases["Covid cases - cumulative total per 100000 population"] <= 5000)]

# plots
bar_plot(who_cases_below, "Nation", ["Covid cases - cumulative total per 100000 population",
                               "Deaths - cumulative total per 100000 population"],
         "Nations with number of cumulative covid cases per 100000 below 10000 and above 5000 in the world", None,
         r'Visualiseringar\covid_who_kumulativ_per100000_between_10000_to_5000_task4.html')

bar_plot(who_cases_above, "Nation", ["Covid cases - cumulative total per 100000 population",
                               "Deaths - cumulative total per 100000 population"],
         "Nations with number of cumulative covid cases per 100000 above 10000 in the world ", None,
         r'Visualiseringar\covid_who_kumulativ_per100000_above_10000_task4.html')

bar_plot(who_cases_above, "Nation", ["Covid cases - cumulative total per 100000 population",
                               "Deaths - cumulative total per 100000 population"],
         "Nations with number of cumulative covid cases per 100000 below 5000 in the world ", None,
         r'Visualiseringar\covid_who_kumulativ_per100000_below_5000_task4.html')

bar_plot(ecdc_vaccine, "ReportingCountry", ["FirstDose", "SecondDose", "Population"],
         "First and second vaccin dose EU/EEA", None, r'Visualiseringar\vaccin_eu_eea_task4.html')
