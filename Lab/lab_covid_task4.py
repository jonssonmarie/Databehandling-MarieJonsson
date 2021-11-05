"""
uppgift 4
länkar:
https://covid19.who.int/table
https://www.ecdc.europa.eu/en/publications-data/data-national-14-day-notification-rate-covid-19
"""

import pandas as pd
import numpy as np
from initial_analyse import analyse
from create_plots import bar_plot
from statistic_covid import statistic_eu_vaccin

# paths to excel files
who_path = r"../Data/WHO COVID-19 global table data November 1st 2021 at 5.02.45 PM.csv"
ecdc_vaccine_path = r"../Data/Data on COVID-19 vaccination in the EUEEA.csv"

# read excel files
covid_cases_who = pd.read_csv(who_path).reset_index()\
    .rename(columns={"index": "Nation", "Cases - cumulative total": "Cases - cumulative total per 100000",
                     "Deaths - cumulative total": "Deaths - cumulative total per 100000",
            "Cases - cumulative total per 100000 population": "Covid cases - cumulative total per 100000 population"})
#
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

# return df with "Region", total dose 1, total dose 2
ecdc_vaccine = sum_per_column(country_list, ecdc_vaccine_cases)
# return percentage for each Region and % dose 1, % dose 2
precentage = statistic_eu_vaccin(country_list, ecdc_vaccine)

# limit data for WHO-cases and drop first row
who_cases = covid_cases_who[["Nation", "WHO Region", "Cases - cumulative total per 100000",
                             "Covid cases - cumulative total per 100000 population",
                             "Deaths - cumulative total per 100000"]].iloc[1:, :].dropna()

# split data for cumulative per 100000 population for easier plots
who_cases_between = who_cases[(who_cases["Deaths - cumulative total per 100000"] < 500)
                              & (who_cases["Deaths - cumulative total per 100000"] > 200)]

who_cases_above = who_cases[(who_cases["Deaths - cumulative total per 100000"] >= 500)]
who_cases_below_5000 = who_cases[(who_cases["Deaths - cumulative total per 100000"] <= 200) &
                                 (who_cases["Deaths - cumulative total per 100000"] > 100)]
who_cases_below_100 = who_cases[(who_cases["Deaths - cumulative total per 100000"] <= 100)]

# plots
bar_plot(who_cases_above, "Nation", ["Cases - cumulative total per 100000",
                                     "Deaths - cumulative total per 100000"],
         "Nations with number of cumulative covid cases per 100000 above 500 in the world ", "Amount", None,
         r'Visualiseringar\task_4_WHO_covid_cumulativ_deaths_per100000_above_500.html')

bar_plot(who_cases_between, "Nation", ["Cases - cumulative total per 100000",
                                       "Deaths - cumulative total per 100000"],
         "Nations with number of cumulative covid cases per 100000 below 500 and above 200 in the world", "Amount", None,
         r'Visualiseringar\task_4_WHO_covid_cumulativ_deaths_per100000_between_200_to_500.html')

bar_plot(who_cases_below_5000, "Nation", ["Cases - cumulative total per 100000",
                                          "Deaths - cumulative total per 100000"],
         "Nations with number of cumulative covid cases per 100000 below 200 in the world ", "Amount", None,
         r'Visualiseringar\task_4_WHO_covid_kumulativ_deaths_per100000_below_200.html')

bar_plot(who_cases_below_100, "Nation", ["Cases - cumulative total per 100000",
                                         "Deaths - cumulative total per 100000"],
         "Nations with number of cumulative covid cases per 100000 below 100 in the world ", "Amount", None,
         r'Visualiseringar\task_4_WHO_covid_kumulativ_deaths_per100000_below_100.html')

bar_plot(ecdc_vaccine, "ReportingCountry", ["FirstDose", "SecondDose", "Population"],
         "First and second vaccin dose EU/EEA", "Amount", None, r'Visualiseringar\task_4_EU_EEA_vaccine.html')

bar_plot(precentage, "ReportingCountry", ["procent_dose1", "procent_dose2"],
         "Percentage dose 1 and dose 2 for each EU/EEA country", "Percentage", None,
         r'Visualiseringar\task_4_EU_EEA_percent.html')
