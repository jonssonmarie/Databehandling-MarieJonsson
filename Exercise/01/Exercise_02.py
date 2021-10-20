"""
2. Clean the data 
  a) As you have conversed with a domain expert you both agree that there are too many missing data 
     to fill in and the proportion is small enough to be safe to just remove.
     Now remove these rows and use your missing-value utility function visualize the remaining NaNs.
  b) The domain expert has told you that you have to fill in the missing age values. 
     Start with visualising the age distribution in the dataset using a histogram.
  c) Check which columns there are in the dataset to see what can be utilised in determining the age.
  d) The column higher seems interesting. Let's see which unique values it can have.
  e) Let's see if we can see some connection between age distribution and higher. Make 3 subplots of age histograms:

Plot 1: same as b)
Plot 2: age distribution when higher is yes
Plot 3: age distribution when higher is no
  f) That was hard to find a connection. When reading dataset source we find alcohol consumption, 
     maybe there is some connection between age and alcohol consumption.
     Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
     Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
     Start with creating a new column called Alcohol, which is a sum of Dalc and Walc columns
  g) Make a barchart for alcohol consumption vs age.
  h) We see that older students tend to drink more, but notice how few 20-22 year-old students we have in the dataset. 
     We can definitely exclude them when computing the missing values. 
     However there are also few 19 year-old students in the dataset, 
     say for simplicity that we can exclude them as well. This leaves:

alcohol level >= 4 -> 16, 17 or 18 years old -> take median to simplify
alcohol level < 4 -> 15 years old
Fill these in and visualize missing values.

Note: could make more stringent by computing percentages based on the distribution
"""