
import pandas as pd

# pipenv install dash


df = pd.read_csv(r"data/AAPL_TIME_SERIES_DAILY.csv")
print(df.head())


class StockDataLocal:
    """ Class method to get and process local stock data"""

    def __init__(self, data_folder_path = "../data/") -> None:
        self._data_folder_path = data_folder_path

    def stock_dataframe(self, stockname) -> list:
        """
        Returns: list of two dataframes, one for daily time series, one for intraday
        """
        stock_df_list = []

        for path_ending in ["_TIME_SERIES_DAILY.csv", "_TIME_SERIES_INTRADAY_EXTENDED.csv"]:
            path = self._data_folder_path + stockname + path_ending
            stock = pd.read_csv(path, index_col=0, parse_dates=True)
            stock.index.rename("Date", inplace=True) 
            # inplace=True gör att man inte behöver göra stock.index = stock.index.rename

            stock_df_list.append(stock)
        return stock_df_list

        """
        sdl = StockDataLocal()
        stock_list = sdl.stock_dataframe("TSLA")
        stocklist[0]
        """




