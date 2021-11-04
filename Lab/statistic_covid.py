import pandas as pd


def statistic_vaccin(vaccin) -> int:
    """
    :param vaccin: dataFrame object
    :return: int (how many people have taken vaccine)
    """
    num_lan = (vaccin.groupby(by="Län").sum()).count().values[0]
    num_kommun = (vaccin.groupby(by="Kommun").sum()).count().values[0]
    num_befolkning = vaccin["Befolkning"].sum()
    print(f"Antal län: {num_lan}")
    print(f"Antal kommuner: {num_kommun}")
    print(f"Antal personer med i vaccinationen: {num_befolkning}")
    return num_befolkning


def statistic_population(age0to15, vaccine_pop_num, swe_pop_num) -> int:
    """
    :param age0to15: dataFrame object
    :param vaccine_pop_num: int     (how many people have taken vaccine in Sweden)
    :param swe_pop_num: int         (Swedens total population)
    :return: None
    """
    num_age0to15 = (age0to15[age0to15["Kön"] == "män"]["Befolkning"].sum() +
                    age0to15[age0to15["Kön"] == "kvinnor"]["Befolkning"].sum()).astype(int)
    num_tot_pop = (swe_pop_num[swe_pop_num["Kön"] == "män"]["Befolkning"].sum() +
                   swe_pop_num[swe_pop_num["Kön"] == "kvinnor"]["Befolkning"].sum()).astype(int)
    percent_age0to15 = (num_age0to15/vaccine_pop_num)*100
    print(f"Antal personer mellan 0-15 år: {num_age0to15}")
    print(f"Sveriges folkmängd: {num_tot_pop}")
    print(f"0-15 år % av befolkningen {percent_age0to15:.2f} %")
    return num_tot_pop


def statistic_eu_vaccin(names, df):
    # "ReportingCountry", "Population", "FirstDose", "SecondDose"
    procent_dos = []
    i = 0
    for name in names:
        dos1 = df[(df["ReportingCountry"] == name)]["FirstDose"]
        dos2 = df[(df["ReportingCountry"] == name)]["SecondDose"]
        nat_pop = df[(df["ReportingCountry"] == name)]["Population"]
        procent_dose1 = ((dos1/nat_pop)*100)[i]
        procent_dose2 = ((dos2/nat_pop)*100)[i]
        summery = [name, procent_dose1, procent_dose2]
        procent_dos.append(summery)
        i += 1
    all_procent = pd.DataFrame(procent_dos, columns=("ReportingCountry", "procent_dose1", "procent_dose2"))
    print(f"EU/EEA vaccinated dose 1 mean: {(all_procent['procent_dose1'].mean()):.1f} %")
    print(f"EU/EEA vaccinated dose 2 mean: {(all_procent['procent_dose2'].mean()):.1f} %\n")
    return all_procent
