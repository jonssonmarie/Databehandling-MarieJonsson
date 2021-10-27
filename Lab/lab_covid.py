"""
Laboration - Covid-19

data:
Covid-19 bekräftade fall : Folkhalsomyndigheten_Covid19.xlsx
Statistik för vaccination mot covid-19 : Folkhalsomyndighetencovid19_Vaccine.xlsx
http://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BE__BE0101__BE0101A/BefolkningNy/?loadedQueryId=102786&timeType=top&timeValue=1

få in documentation också!
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly
import plotly.graph_objects as go


# paths to excel files
covid_path = r"../Data/Folkhalsomyndigheten_Covid19.xlsx "
vaccin_path = r"../Data/Folkhalsomyndigheten_Covid19_Vaccine.xlsx"
swe_tot_population_path = r"../Data/Befolkning_Sverige_20211027.xlsx"
swe_pop_age0to15_path = r"../Data/Befolkning_age0to15_20211027.xlsx"

# read excel files
covid_cases = pd.read_excel(covid_path, sheet_name="Veckodata Riket")
vaccin_cases = pd.read_excel(vaccin_path, sheet_name="Vaccinerade kommun och ålder")
swe_tot_population = pd.read_excel(swe_tot_population_path).rename(columns={"Unnamed: 1": "Kön",  "Unnamed: 2": "Befolkning"})
swe_pop_age0to15 = pd.read_excel(swe_pop_age0to15_path).rename(columns={"Unnamed: 1": "Kön",  "Unnamed: 2": "Befolkning"})

def inital_analyse(df):
    #print(df.info(), "\n")
    #print(df.describe(), "\n")
    print(df.value_counts(), "\n")
    print(df.head(), "\n")
    print(df.tail(), "\n")
    print(df.columns, "\n")
    print(df.index, "\n")


# inital_analyse(covid_cases)
#inital_analyse(vaccin_cases)
#inital_analyse(swe_tot_population)
#inital_analyse(swe_pop_age0to15)

# Slå ihop kolumnerna "år" och "veckonummer" till en kolumn med namn "Vecka" med följande format: 2021v41
def add_yearweek(df):
    df["Vecka"] = df["år"].astype(str) + 'v' + df["veckonummer"].astype(str)
    # print(covid_cases["Vecka"])
    return df["Vecka"]


add_yearweek(covid_cases)
#inital_analyse(covid_cases)


def plot_covid_2x2(df):
    fig, ax = plt.subplots(2, 2, dpi=100, figsize=(15, 10))
    # För deluppgifterna c-f, använd både Seaborn och Plotly express. För Seaborn, använd subplots så du får 2x2
    # grid med graferna.  MISSAT !!!!! Och vad ska jag använda plotly express till?
    plt.grid()  # får bara grid på sista ploten 1,1  Varför?    FIXA
    sns.lineplot(data=df, x="Vecka", y="Antal_avlidna_vecka", ax=ax[0, 0], label="Avlidna per vecka")\
        .set(title="Antal avlidna per vecka från 2020v6 till 2021v41")
    sns.lineplot(data=df, x="Vecka", y="Antal_fall_vecka", ax=ax[0, 1], label="Nya fall per vecka")\
        .set(title="Antal nya fall per vecka från 2020v6 till 2021v41")
    sns.lineplot(data=df, x="Vecka", y="Antal_avlidna_vecka", ax=ax[1, 0], label="Avlidna per vecka")\
        .set(title="Antal avlidna och nya fall från 2020v6 till 2021v41")
    sns.lineplot(data=df, x="Vecka", y="Antal_fall_vecka",ax=ax[1, 0], label="Nya fall per vecka")
    sns.lineplot(data=df, x="Vecka", y="Kum_antal_fall", ax=ax[1, 1], label="Antal avlidna per vecka")\
        .set(title="Antal Kummulativa fall från 2020v6 till 2021v41")
    plt.legend()
    plt.savefig(r"Visualiseringar/covid_data.png")
    plt.show()


plot_covid_2x2(covid_cases)

"""
a) Hur många län finns representerade i datasetet?
b) Hur många kommuner finns representerade i datasetet?
c) Hur stor är befolkningen som är representerad i datasetet?
d) Beräkna hur många barn under 16 år det finns i Sverige. Du får leta upp statistik på hur stor totala
befolkningen är i Sverige.
e) Rita stapeldiagram för andel med minst 1 dos per län och andel färdigvaccinerade per län
f) Rita ett stapeldiagram med län i x-axeln och staplar för befolkning > 16år, antal minst 1 dos och antal
färdigvaccinerade.

"""
# SNYGGA UPP MED DEF OCH PRINT F FÖR A -D
num_lan = (vaccin_cases.groupby(by="Län").sum()).count().values[0]
num_kommun = (vaccin_cases.groupby(by="Kommun").sum()).count().values[0]
num_befolkning = (vaccin_cases["Befolkning"].sum())
num_age0to15 = (swe_pop_age0to15[swe_pop_age0to15["Kön"] == "män"]["Befolkning"].sum() +
               swe_pop_age0to15[swe_pop_age0to15["Kön"] == "kvinnor"]["Befolkning"].sum()).astype(int)
num_tot_pop = (swe_tot_population[swe_tot_population["Kön"] == "män"]["Befolkning"].sum() +
              swe_tot_population[swe_tot_population["Kön"] == "kvinnor"]["Befolkning"].sum()).astype(int)
percent_age0to15 = (num_age0to15/num_befolkning)*100
print(num_lan)
print(num_kommun)
print(num_befolkning)
print(num_age0to15)
print(num_tot_pop)
print(percent_age0to15)

lan_namn = vaccin_cases["Län_namn"].unique()


def sum_column(lan_name, df):
    """ calculate sum from a column"""
    dos1_dos2 = []
    for name in lan_name:
        dos1 = np.sum(df[df["Län_namn"] == name]["Antal minst 1 dos"])
        dos2 = np.sum(df[df["Län_namn"] == name]["Antal färdigvaccinerade"])
        summery = [name, dos1, dos2]
        dos1_dos2.append(summery)
    all_dos = pd.DataFrame(dos1_dos2, columns=("Län_namn", "Antal minst 1 dos", "Antal färdigvaccinerade"))
    return all_dos


sum_column(lan_namn, vaccin_cases)


def stapel_plot(df):
    # e) Rita stapeldiagram för andel med minst 1 dos per län och andel färdigvaccinerade per län
    # Plotly express
    fig = px.bar(df, x="Län_namn", y="Antal minst 1 dos",
                 labels={"Län_namn": "Län", "Antal minst 1 dos": "Antal som tagit 1 dos"},title="Antal som tagit 1 dos per län")
    fig2 = px.bar(df, x="Län_namn", y="Antal färdigvaccinerade",
                  labels={"Län_namn":"Län", "Antal färdigvaccinerade": "Antal som tagit 2 doser per län"},
                  title="Antal och dos 2 per län")
    # html file
    plotly.offline.plot(fig, filename=r'Visualiseringar/dos1_vaccinated.html')
    plotly.offline.plot(fig2, filename=r'Visualiseringar/dos2_vaccinated.html')


#stapel_plot(sum_column(lan_namn, vaccin_cases))

"""
# Hur få in båda i samma plot så man kan jämföra?
fig = go.Figure(data=[
        px.Bar(name="Antal minst 1 dos", x=lan_namn, y=vaccin_cases["Antal minst 1 dos"]),
        px.Bar(name="Antal färdigvaccinerade", x=lan_namn, y=vaccin_cases["Antal färdigvaccinerade"]
           ])
#change bar mode
fig.update_layout(barmode='group')
fig.show()"""

