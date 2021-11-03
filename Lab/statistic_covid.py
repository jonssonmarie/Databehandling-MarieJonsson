
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
