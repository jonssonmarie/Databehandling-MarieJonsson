
def analyse(df):
    """
    :param df: DataFrame object
    :return: None
    """
    print(df.info(), "\n")
    print(df.describe(), "\n")
    print(df.value_counts(), "\n")
    print(df.head(), "\n")
    print(df.tail(), "\n")
    print(df.columns, "\n")
    print(df.index, "\n")
    