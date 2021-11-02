
import pandas as pd
from dash import dcc, html
# dcc interaktiva saker, html för html element
import dash 
from load_data import StockDataLocal
from dash.dependencies import Output, Input
import matplotlib.pyplot as plt
import plotly_express as px

stock_data_object = StockDataLocal()

symbol_dict = dict(APPL="Apple", NVDA="Nividia", TSLA="Tesla", IBM="IBM")

stock_options_dropdown =[{"label": name, "value": symbol} for symbol, name in symbol_dict.items()]

df_dict = {symbol: stock_data_object.stock_dataframe(symbol) for symbol in symbol_dict }

slider_marks = {i: mark for i, mark in enumerate(
    ["1 day", "1 week", "1 month", "3 months", "1 year", "5 years", "Max"]
    )}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stocks viewer"),             # H1  = header one H2("This is a cool app")
    html.P("Choose a stock"),    
    dcc.Dropdown(id='stock-picker-dropdown', className='',
        options=[],
        value='APPL'  # gör att den börjar på APPL
                ),
    
    dcc.Graph(id='stock-graph', className=''),
    dcc.Slider(id='time-slider', className='',
        min = 0, 
        max=6, 
        step=None, 
        value = 2,
        marks = slider_marks)      
])

@app.callback(
    Output("stock_graph", "figure"),  # output är bakgrund (axlar)
    Input("stock-picker-dropdown", "value"),   # input är graph
    Input("time-slider", "value")
            )

def update_graph(stock, time_index):
    dff_daily, dff_intraday = df_dict[stock]

    dff = dff_intraday if time_index <= 2 else dff_daily

    fig = px.line(dff, x= dff.index, y="close")
    return fig # fig object goes int Output property i.e. figure property
    



if __name__ == "__main__":
    app.run_server(debug=True)











