"""
vs code
pipenv install plotly
pipenv install plotly-express
pipenv install nbformat

"""
import plotly
import plotly_express as px
import nbformat

gapminder = px.data.gapminder()
print(gapminder.head())

print(gapminder.describe())  #.transpose()
print(gapminder.info())
print(gapminder["country"].unique().__len__(), len(gapminder["country"].unique()))  # __len__ overloadar

# på ett bra sätt
"""nordic = gapminder[gapminder["country"].isin(["Sweden", "Norway", "Denamrk", "Iceland", "Finland"])]
print(nordic)
print(nordic["country"].value_counts())"""

# samma sak fast på annat sätt
bool_series = gapminder["country"].isin(["Sweden", "Norway", "Denamrk", "Iceland", "Finland"])
nordic = gapminder[bool_series]
#print(nordic)
print(nordic["country"].value_counts())

sweden = gapminder[gapminder["country"] == "Sweden"]

fig0 = px.bar(sweden, x="year", y="pop", labels= {"pop": "Population", "year": "Year"},
             title="Sweden population 1952-2007")
# labels  gör att man kan ändra texten för x, y som tas från df column
#fig0.show()

nordic2007 = nordic[nordic["year"] == 2007]
#print(nordic2007)
fig1 = px.bar(nordic2007, x="country", y="gdpPercap", color="country")
#fig1.show()

# Line chart

fig2 = px.line(sweden, x="year", y="gdpPercap", title="GDP per capita in Sweden 1952 - 2007")
#fig2.show()

fig3 = px.line(nordic, x="year", y="gdpPercap", color="country", title="GDP per capita in Sweden 1952 - 2007",
              labels=dict(gdpPercap="GDP/capita", year="Year", country="Country"))
fig3.update_layout(hovermode="x")
fig3.update_xaxes(showspikes=True,
                spikedash="solid",
                spikemode="across",
                spikecolor="green",
                spikesnap="cursor")
#fig3.show()

# Pie chart
fig4 = px.pie(nordic2007, values="pop", title="Population of nordic countries 2007", names="country")
fig4.update_traces(textinfo="label+percent")
#fig4.show()


# Bubble chart
fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", color="country", size_max=70, log_x=True,
                 animation_frame="year",title="Gapminder", range_x=[100,100000], range_y=[25,90])
fig.show()