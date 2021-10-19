"""
1. Cities in Sweden - create dataset
Create this DataFrame from scratch:

    Kommun	   Population
0	Malmö	    347949
1	Stockholm	975551
2	Uppsala	    233839
3	Göteborg	583056
  a) Use your DataFrame to print out all the cities.
  b) Select only the row which contains Göteborg. Do this by using the name Göteborg.
  c) Sort the cities by population from largest to smallest.
  d) Filter out the three largest cities.
  e) The whole population in Sweden 2020 is 10379295.
     Use this number to create a new column in your sorted DataFrame named: Population (%).
     This column should be filled with percentage of the Swedish population for each city.
"""
import pandas as pd

cities = {"Kommun" : ["Malmö", "Stockholm", "Uppsala", "Göteborg"], "Population" : [347949, 975551, 233839, 583056]}

# a) print dataframe
df_cities = pd.DataFrame(cities)  # create a dataframe
only_cities = df_cities["Kommun"]  # get the cities for print
print(f"\na) dataFrame:\n{only_cities}")

# b) print row for Göteborg
gothenburg = df_cities[df_cities["Kommun"] == "Göteborg"]
print(f"\nb) Göteborg:\n {gothenburg}")

# c) sort cities
cities_sorted = df_cities.sort_values(by="Population", ascending=False).head()
print(f"\nc) Sorted by population: \n{cities_sorted}")

# d) Filter
largest_3 = cities_sorted.iloc[:3]
print(f"\nd) Largest 3: \n{largest_3}")

# e) create a new column in existing dataframe named: Population (%).
#    This column should be filled with percentage of the Swedish population for each city
swe_pop = 10379295
df_cities["Population (%)"] = (df_cities["Population"]/swe_pop*100).round(2)  # adding new column and round %
sorted = df_cities.sort_values(by="Population", ascending=False)  # sort again after adding
print(f"\ne) Updated dataframe:\n {sorted}")
