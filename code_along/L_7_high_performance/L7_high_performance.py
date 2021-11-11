"""
High performance

Python:
mask = ( x > 0.5) & ( y < 0.5)

ex: df = df[df[mask]]

itermediate variables in memory
Python:
tmp1 = x < 0.5
tmp = y > 0.5
mask tmp1 & tmp2

Cn use pd.eval("") -> performs elementwise directly using numexpr
Good for compound expressions

install numexpr och Bottleneck
"""

import numpy as np
import pandas as pd
import time
import timeit
#import bottleneck as bn


start = time.time()
nrows, ncols = 100000, 100

df1, df2, df3, df4 = [pd.DataFrame(np.random.randn(nrows,ncols)) for _ in range(4)]
# _  använd för att ingen variabel används
# df1.info ger hur mycket minne som används av df1

#timeit.timeit(df1 + df2 + df3 + df4)
plain = df1 + df2 + df3 + df4
sum_eval = pd.eval("df1 + df2 + df3 + df4")

sum_eval.equals(plain)


rolls = pd.DataFrame(np.random.randint(1,6,(6,3)), columns=["Die1","Die2", "Die3"])
rolls.eval("Sum = Die1 +Die2 +Die3", inplace=True)
print(rolls)
high = 10
rolls.eval("Winner = Sum > @high", inplace=True) # @ger tillgång till lokal varibale inom "scopet"

# filter out "traditional" way
rolls[rolls["Sum"] <= high]


rolls.query("Sum <= @high")

os = pd.read_csv("athlete_events.csv")

print(os.head())

#%timeit os[os["NOC"] == "SWE"] # % är en dunderfunk som bara funkar i jupyter
#%timeit os.query("NOC == 'SWE'")

#%timeit os[os["NOC"] == "SWE"]
#%timeit os.query("Sex == 'F' & Height > 100 & NOC == 'SWE'")

# enhancing performance in pandas
# magic %prun
# %cython

end = time.time()
print("\nThe time of execution of above program is :", end - start)

