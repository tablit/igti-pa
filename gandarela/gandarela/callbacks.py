""" from dash.dependencies import Input, Output
import app  # Your app.py

# Define your callbacks here
# Example:
@app.callback(Output('output-component', 'property'), [Input('input-component', 'value')])
def update_output(value):
    # Callback logic
    return new_value
    """

from dash.dependencies import Input, Output
import plotly.express as px

def register_callbacks(app,df,cad):

    @app.callback(
        Output('fund-performance-graph', 'figure'),
        [Input('comparison-funds-dropdown', 'value'),
         Input('main-fund-dropdown', 'value')]
    )
    def update_graph(comparison_funds,main_fund):
        # Filter DataFrame based on selected fund names
        selected_funds = [main_fund] + comparison_funds if main_fund else comparison_funds
        filtered_df = df[df['DENOM_SOCIAL'].isin(selected_funds)]
        print(f"Selected funds: {selected_funds}")
        print(f"DF shape: {filtered_df.shape}")
        

        # Create a figure using the filtered DataFrame
        fig = px.line(filtered_df, 
                    x='Month-Year',  # Ensure your DataFrame has this column
                    y='PR_RENTAB_MES',  # And this one for performance metrics
                    color='DENOM_SOCIAL',  # Color lines by fund name
                    title='Performance Histórica dos fundos')
        fig.update_layout(xaxis_title='Date', 
                  yaxis_title='Performance Mensal (%)',
                  legend_title='Fundos')

        return fig
    
    
    @app.callback(
        Output('main-fund-markdown', 'children'),
        [Input('main-fund-dropdown', 'value')]
    )
    def update_markdown(main_fund):
        # Logic to obtain data based on selected value
        cad_df = cad.copy()
        main_fund_data = cad_df[cad_df['DENOM_SOCIAL'].isin([main_fund])]

        # Select only one fund row
        fund_info = main_fund_data.iloc[0]  # TODO: filter based on fund situation (SIT column)

        # Formatting the fund information in Markdown
        markdown_content = f"""
        ## Informações Societárias

        - **Razão Social**: {fund_info['DENOM_SOCIAL']}
        - **CNPJ**: {fund_info['CNPJ_FUNDO']}
        - **Data Inicial**: {fund_info['DT_INI_ATIV']}
        - **Tipo do Fundo**: {fund_info['TP_FUNDO']} 
        - **Administrador**: {fund_info['ADMIN']}
        - **Classe**: {fund_info['CLASSE']}
        - **Classe ANBIMA**: {fund_info['CLASSE_ANBIMA']}
        - **Gestor**: {fund_info['GESTOR']}
        """

        return markdown_content


