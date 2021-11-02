
import pandas as pd
from dash import dcc, html
# dcc interaktiva saker, html för html element
import dash 

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Stocks viewer"),             # H1  = header one
    html.H2("This is a cool app")
])

if __name__ == "__main__":
    app.run_server(debug=True)












