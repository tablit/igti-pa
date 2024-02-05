
from dash import html, dcc, dash_table
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


def get_layout(lamina,cad):
    dropdown_options = [{'label': name, 'value': name} for name in lamina['DENOM_SOCIAL'].unique()]
    return html.Div([
        html.H1("Comparativo de Fundos"),
        html.Div(children='Escolha abaixo o fundo a ser analizado'),
        dcc.Dropdown(
            id='main-fund-dropdown',
            options=dropdown_options,
            value=[],
            multi = False  # Default value
        ),
        dash_table.DataTable(
            id='main-fund-societary-table'
            ),
        html.H2("Performance histórica do fundo"),
        html.Div(children="Escolha outros fundos para comparar a performance"),
        dcc.Dropdown(
            id='comparison-funds-dropdown',
            options=dropdown_options, #TODO: remove main-fund from list
            value=[],
            multi = True  # Default value
        ),
        dcc.Graph(id = 'fund-performance-graph')
    ])

