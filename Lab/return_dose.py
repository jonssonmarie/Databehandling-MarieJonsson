
def dose_region(df, region, dos_num) -> object:
    """Sort vaccination status per Län/Region
    :param df: DataFrame object
    :param region: str
    :param dos_num:  str
    :return: DataFrame object
    """
    dos_region = df[(df["Region"] != region) & (df["Vaccinationsstatus"] == dos_num) & (df["Åldersgrupp"] != "Totalt")]
    return dos_region


def dose_sverige(df, region, dos_num) -> object:
    """ Sort vaccination status for Sweden
    :param df: DataFrame object
    :param region: str
    :param dos_num: str
    :return: DataFrame object
    """
    dos_sverige = df[(df["Region"] == region) & (df["Vaccinationsstatus"] == dos_num) & (df["Åldersgrupp"] != "Totalt")]
    return dos_sverige


def dose_sverige_tot(df, region) -> object:
    """Sort vaccination on total dose 1 and 2 per Län/Region
    :param df: DataFrame object
    :param region: str
    :param dos_num: str
    :return: DataFrame object
    """
    dos_sverige = df[(df["Region"] == region) & (df["Åldersgrupp"] == "Totalt")]
    return dos_sverige
