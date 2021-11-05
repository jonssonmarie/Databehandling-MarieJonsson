import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly


def bar_plot(df, x_value, y_value, an_title, y_name, color_name, file_path) -> None:
    """
    :param df: dataFrame object
    :param x_value: str     for x axis
    :param y_value: str     for y axis
    :param an_title: str    for setting title
    :param color_name: str  for setting color
    :param file_path: str   path to place to save the plot
    :return: None
    """
    fig = px.bar(df, x=x_value, y=y_value, barmode='group', color=color_name,
                 labels={"variable": "", "value": y_name},
                 title=an_title)
    plotly.offline.plot(fig, filename=file_path)


def pie_plot(df) -> None:
    """
    :param df: dataFrame object
    :return: None
    """
    fig1 = px.pie(df, values="Totalt_antal_avlidna", title="Antal avlidna per kön", names="Kön")
    fig1.update_traces(textinfo="label+percent")
    plotly.offline.plot(fig1, filename=r'Visualiseringar\task_3_totalt_antal_avlidna_per_kön.html')


def compare_infected_iva_plot(df) -> None:
    """
    Number of covid cases per week and number of intensive care cases per week
    :param df: dataFrame object
    :return: None
    """
    df = df.rename(columns={"Antal_fall_vecka": "Antal fall vecka",
                            "Antal_nyaintensivvårdade_vecka": "Antal intensivvårdade vecka"})
    fig = px.line(df, x="Vecka", y=["Antal fall vecka", "Antal intensivvårdade vecka"],
                  title="Antal covidfall och antal IVA vårdade",
                  labels={"variable": "", "value": "Antal personer"})
    fig.update_yaxes(type="log")
    plotly.offline.plot(fig, filename=r'Visualiseringar\task_3_Antal_covid_och_iva_vårdade.html')


def adjust_plot(place, y_label) -> None:
    """
    :param place: ax[ , ] with position in subplot
    :param y_label: str for y-axel
    :return: png file
    """
    n = [i for i in np.arange(0, 90, 5)]
    place.set_xticks(n, minor=False)
    place.tick_params(axis='x', rotation=90)
    place.set_yscale('log')
    place.set_ylabel(y_label)
    place.grid()
    plt.tight_layout()
    plt.savefig(r"Visualiseringar\task_1_covid_data.png")


def plot_covid_2x2(df) -> None:
    """
    :param df: DataFrame object
    :return: None
    """
    fig, ax = plt.subplots(2, 2, dpi=100, figsize=(18, 12))

    # plot first subplot
    sns.lineplot(data=df, x="Vecka", y="Antal_avlidna_vecka", ax=ax[0, 0], label="Avlidna per vecka")\
        .set(title="Antal avlidna per vecka från 2020v6 till 2021v41")
    adjust_plot(ax[0, 0], "Antal avlidna vecka")

    # plot second subplot
    sns.lineplot(data=df, x="Vecka", y="Antal_fall_vecka", ax=ax[0, 1], label="Nya fall per vecka")\
        .set(title="Antal nya fall per vecka från 20v6 till 21v41")
    adjust_plot(ax[0, 1], "Antal fall vecka")

    # plot third subplot with both lineplots
    sns.lineplot(data=df, x="Vecka", y="Antal_avlidna_vecka", ax=ax[1, 0], label="Avlidna per vecka")\
        .set(title="Antal avlidna och nya fall från 20v6 till 21v41")
    sns.lineplot(data=df, x="Vecka", y="Antal_fall_vecka", ax=ax[1, 0], label="Nya fall per vecka")\
        .set(title="Nya fall och avlidna per vecka")
    adjust_plot(ax[1, 0], "Antal avlidna vecka")

    # plot fourth subplot
    sns.lineplot(data=df, x="Vecka", y="Kum_antal_fall", ax=ax[1, 1], label="Antal avlidna per vecka")\
        .set(title="Antal kumulativa fall från 20v6 till 21v41")
    adjust_plot(ax[1, 1], "Kum antal fall")
