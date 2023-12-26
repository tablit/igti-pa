# %%

import plotly.express as px
import pandas as pd
import csv
import re

df = lamina_rentab_mes_202311 = pd.read_csv("data/if_lamina/lamina_fi_rentab_mes_202311.csv",sep=";",encoding='ISO-8859-1', quoting=csv.QUOTE_NONE)



# Data Preparation

# Ensuring correct data types
df['DT_COMPTC'] = pd.to_datetime(df['DT_COMPTC'], format='%Y-%m-%d')
df['PR_RENTAB_MES'] = pd.to_numeric(df['PR_RENTAB_MES'], errors='coerce')
df['PR_VARIACAO_INDICE_REFER_MES'] = pd.to_numeric(df['PR_VARIACAO_INDICE_REFER_MES'], errors='coerce')
df['PR_PERFM_INDICE_REFER_MES'] = pd.to_numeric(df['PR_PERFM_INDICE_REFER_MES'], errors='coerce')

# Finding the CNPJ of the top performer fund from the original dataset
cnpj_top_performer = df.loc[df['PR_RENTAB_MES'].idxmax(), 'CNPJ_FUNDO']

# Removing the top performer fund from the dataset
df_without_top_performer = df[df['CNPJ_FUNDO'] != cnpj_top_performer]

# Displaying the first few rows of the dataset without the top performer
df_without_top_performer_head = df_without_top_performer.head()
df_without_top_performer_head

# Now, let's find the top performing funds based on 'PR_RENTAB_MES'
# Assuming 'top' means the highest positive returns
top_performing_funds = df_without_top_performer_head.nlargest(10, 'PR_RENTAB_MES')[['DENOM_SOCIAL', 'PR_RENTAB_MES']]

top_performing_funds


# Assuming 'top_performing_funds' is the DataFrame you have from the previous step
fig = px.bar(top_performing_funds, 
             x='PR_RENTAB_MES', 
             y='DENOM_SOCIAL', 
             orientation='h',
             title='Top 10 Performing Investment Funds in Brazil (Latest Month)',
             labels={'PR_RENTAB_MES': 'Monthly Performance (%)', 'DENOM_SOCIAL': 'Fund Name'})

# Improving layout for readability
fig.update_layout(yaxis={'categoryorder':'total ascending'}, 
                  xaxis_title="Monthly Performance (%)",
                  yaxis_title="Fund Name",
                  showlegend=False)

fig.show()

# %%

# Filtering the dataset for the month of November (MES_RENTAB == 11)
november_data = df_without_top_performer[df_without_top_performer['MES_RENTAB'] == 11]

# Finding the top 5 performing funds in November based on 'PR_RENTAB_MES'
top_5_november_funds = november_data.nlargest(5, 'PR_RENTAB_MES')['CNPJ_FUNDO'].unique()

# Filtering the original dataset for the historical data of these top 5 funds
historical_data_top_5_november = df_without_top_performer[df_without_top_performer['CNPJ_FUNDO'].isin(top_5_november_funds)]
historical_data_top_5_november['Year'] = historical_data_top_5_november['DT_COMPTC'].dt.year
historical_data_top_5_november['Month-Year'] = pd.to_datetime(historical_data_top_5_november['Year'].astype(str) + '-' + historical_data_top_5_november['MES_RENTAB'].astype(str))

# Simplifying the 'DENOM_SOCIAL' names by keeping only the part before "fundo de investimento" or similar suffixes
def simplify_fund_name_v2(name):
    # Pattern to find the position of the suffix "fundo de investimento" or similar
    pattern = re.compile(r"\bfundo de investimento\b|\bfundo de invest\b|\bfi\b|\bfia\b|\bfim\b|\bficfia\b|\bficfi\b|\bfic fim\b|\bfund\b|\bfundos\b|\binvestment fund\b|\binvestimento em ações\b|\binvestimento multimercado\b", flags=re.IGNORECASE)

    # Search for the pattern
    match = pattern.search(name)
    if match:
        # Return the part of the string before the suffix
        return name[:match.start()].strip()
    else:
        # Return the original name if no suffix is found
        return name

# Applying the function to create a new simplified name column
historical_data_top_5_november['Simplified_Name_V2'] = historical_data_top_5_november['DENOM_SOCIAL'].apply(simplify_fund_name_v2)



# Creating a line graph to show the historical performance of these funds
fig = px.line(historical_data_top_5_november, 
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


fig.show()

# %%
