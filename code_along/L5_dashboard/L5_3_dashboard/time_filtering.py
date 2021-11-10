from datetime import datetime
from dateutil.relativedelta import relativedelta


now = datetime.now()
yesterday = now - relativedelta(days=10)
print(yesterday)

def filter_time(df, days=10):
    last_day = df.index[0].date()  # .date() ger datumet och slänger bort tiden
    start_day = last_day - relativedelta(days = days)
    df = df.sort_index().loc[start_day:last_day]  # sort_index() - skips varning
    



