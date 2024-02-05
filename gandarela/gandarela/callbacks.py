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
        [Output('main-fund-societary-table','data'), # Update societary table data
         Output('main-fund-societary-table','columns')], # Update societary table columns
        Input('main-fund-dropdown','value')
    )
    def update_table(main_fund):
        # Logic to filter data based on the selected value
        cad_df = cad.copy()
        main_fund_data = cad_df[cad_df['DENOM_SOCIAL'].isin([main_fund])]

        # Prepare the data for the DataTable
        data = main_fund_data.to_dict('records')
        columns = [{"name": i, "id": i} for i in main_fund_data.columns]

        return data, columns


