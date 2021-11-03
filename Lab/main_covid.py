"""
Laboration - Covid-19

Sveriges befolkning 
http://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BE__BE0101__BE0101A/BefolkningNy/?loadedQueryId=102786&timeType=top&timeValue=1
"""
import pandas as pd
import numpy as np
import time
from initial_analyse import analyse
from many_plots import bar_plot, pie_plot, compare_infected_iva_plot, plot_covid_2x2
from statistic_covid import statistic_vaccin, statistic_population
from return_dose import dose_region, dose_sverige, dose_sverige_tot
import lab_covid_task4


def add_yearweek(df) -> object:
    """
    :param df: dataFrame object
    :return: dataFrame column
    """
    """ Sets column 'år' and 'veckonummer' to one column with format '2021v41' """
    df["Vecka"] = df["år"].astype(str) + 'v' + df["veckonummer"].astype(str)
    return df["Vecka"]


def sum_per_column(names, df) -> object:
    """
    calculate sum from a columns for a key and save to a dataframe
    :param names: list of strings
    :param df: dataFrame object
    :return: dataFrame object
    """
    dos1_dos2 = []
    for name in names:
        dos1 = np.sum(df[(df["Län_namn"] == name) & (df["Ålder"] != "12-15")]["Antal minst 1 dos"])
        dos2 = np.sum(df[(df["Län_namn"] == name) & (df["Ålder"] != "12-15")]["Antal färdigvaccinerade"])
        summery = [name, dos1, dos2]
        dos1_dos2.append(summery)
    all_dos = pd.DataFrame(dos1_dos2, columns=("Län_namn", "Antal minst 1 dos", "Antal färdigvaccinerade"))\
        .rename(columns={"Län_namn": "Län", "Antal minst 1 dos": "dos 1", "Antal färdigvaccinerade": "dos 2"})
    return all_dos


def main():
    start = time.time()
    covid_path = r"../Data/Folkhalsomyndigheten_Covid19.xlsx"
    vaccine_path = r"../Data/Folkhalsomyndigheten_Covid19_Vaccine.xlsx"
    swe_population_path = r"../Data/Befolkning_Sverige_20211027.xlsx"
    swe_pop_age0to15_path = r"../Data/Befolkning_age0to15_20211027.xlsx"

    # read excel files
    covid_cases = pd.read_excel(covid_path, sheet_name="Veckodata Riket")
    vaccine_cases = pd.read_excel(vaccine_path, sheet_name="Vaccinerade kommun och ålder")
    swe_population = pd.read_excel(swe_population_path)\
        .rename(columns={"Unnamed: 1": "Kön", "Unnamed: 2": "Befolkning"})
    swe_pop_age0to15 = pd.read_excel(swe_pop_age0to15_path)\
        .rename(columns={"Unnamed: 1": "Kön", "Unnamed: 2": "Befolkning"})
    amount_per_agegroup = pd.read_excel(covid_path, sheet_name="Totalt antal per åldersgrupp")
    covid_per_sex = pd.read_excel(covid_path, sheet_name="Totalt antal per kön")
    vaccine_agegroup = pd.read_excel(vaccine_path, sheet_name="Vaccinerade ålder")

    analyse(covid_cases)
    # analyse(vaccin_cases)
    # analyse(swe_tot_population)
    # analyse(swe_pop_age0to15)

    add_yearweek(covid_cases)
    plot_covid_2x2(covid_cases)
    num_befolkning = statistic_vaccin(vaccine_cases)
    lan_namn = vaccine_cases["Län_namn"].unique()

    dos1_dos2 = sum_per_column(lan_namn, vaccine_cases)
    bar_plot(dos1_dos2, "Län", ["dos 1", "dos 2"], "Antal dos 1 respektive dos 2 per län", None,
             r'Visualiseringar\dos1_dos2_task_2.html')

    bar_plot(covid_per_sex, "Kön", ["Totalt_antal_intensivvårdade", "Totalt_antal_avlidna"],
             "Antal covidfall per kön", None, r'Visualiseringar\totalt_iva_avlidna_per_sex_task3.html')

    bar_plot(amount_per_agegroup, "Åldersgrupp", ["Totalt_antal_intensivvårdade", "Totalt_antal_avlidna"],
             "Totalt antal per åldersgrupp", None, r'Visualiseringar\Totalt_antal_per_åldersgrupp_task3.html')

    dos1_region = dose_region(vaccine_agegroup, "| Sverige |", "Minst 1 dos")
    bar_plot(dos1_region, "Region", ["Antal vaccinerade"], "Antal dos 1 per åldersgrupp per region",
             "Åldersgrupp", r'Visualiseringar\Antal_vaccinerade_åldersgrupp_dos1_region_task2e.html')

    dos2_region = dose_region(vaccine_agegroup, "| Sverige |", "Färdigvaccinerade")
    bar_plot(dos2_region, "Region", ["Antal vaccinerade"], "Antal dos 2 per åldersgrupp per region",
             "Åldersgrupp", r'Visualiseringar\Antal_vaccinerade_åldersgrupp_dos2_region_task2e.html')

    dos1_sverige = dose_sverige(vaccine_agegroup, "| Sverige |", "Minst 1 dos")
    bar_plot(dos1_sverige, "Åldersgrupp", ["Antal vaccinerade"], "Antal dos 1 per åldersgrupp i Sverige",
             "Åldersgrupp", r'Visualiseringar\Antal_vaccinerade_åldersgrupp_dos1_Sverige_task2f.html')

    dos2_sverige = dose_sverige(vaccine_agegroup, "| Sverige |", "Färdigvaccinerade")
    bar_plot(dos2_sverige, "Åldersgrupp", ["Antal vaccinerade"], "Antal dos 2 per åldersgrupp i Sverige",
             "Åldersgrupp", r'Visualiseringar\Antal_vaccinerade_åldersgrupp_dos2_Sverige_task2f.html')

    # en extra då jag ville se doser mot totala folkmängden
    vaccin_sverige_totalt = dose_sverige_tot(vaccine_agegroup, "| Sverige |")
    sve_befolking = statistic_population(swe_pop_age0to15, num_befolkning, swe_population)
    lst = ["| Sverige |", "Totalt", sve_befolking, 0.0, "Totala befolkning"]
    swe_befolkning = pd.DataFrame(lst, index=("Region", "Åldersgrupp", "Antal vaccinerade", "Andel vaccinerade", "Vaccinationsstatus"  )).T
    vaccin_befolkning = pd.concat((vaccin_sverige_totalt, swe_befolkning), axis=0)

    bar_plot(vaccin_befolkning, "Vaccinationsstatus", "Antal vaccinerade",  "Antal vaccinerade i Sverige och befolkningsmängd",
             "Vaccinationsstatus", r'Visualiseringar\Antal_vaccinerade_totalt_Sverige_extra.html')

    pie_plot(covid_per_sex)

    compare_infected_iva_plot(covid_cases)

    end = time.time()
    print("\nThe time of execution of above program is :", end - start)


if __name__ == '__main__':
    main()
