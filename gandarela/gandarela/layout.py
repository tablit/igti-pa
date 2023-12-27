
from dash import html, dcc
import data
import plotly.express as px

def create_graph(df):
    # Here you'll use df to create and return your plotly figure
    fig = px.line(df, 
              x='Month-Year', 
              y='PR_RENTAB_MES', 
              color='Simplified_Name_V2',
              labels={'PR_RENTAB_MES': 'Monthly Performance (%)', 'DT_COMPTC': 'Date', 'CNPJ_FUNDO': 'Fund CNPJ'},
              title='Historical Monthly Performance of Top 5 Performing Funds in November')

    fig.update_layout(xaxis_title='Date', 
                  yaxis_title='Monthly Performance (%)',
                  legend_title='Fund CNPJ')

    # Set the x-axis to show each month
    fig.update_xaxes(dtick="M1", tickformat="%b %Y")
    return fig


def get_layout():
    df = data.load_data()
    df = data.prepare_november_data(df)
    graph = create_graph(df)

    return html.Div([
        html.H1("Dash Application"),
        dcc.Graph(figure=graph),
        # Other layout elements...
    ])