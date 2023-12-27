import pandas as pd
import plotly.express as px


""" def load_and_prepare_data():
    # Load your data and perform necessary transformations
    # ...

    return data

def create_figure(data):
    # Assuming data is your DataFrame
    # Create and return a Plotly figure based on the data
    # ...

    return fig """

#%%
import pandas as pd
import csv
import re
import os
from dotenv import load_dotenv
import boto3
from io import BytesIO



def load_data():
    # Load environment variables from .env file
    load_dotenv()
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    session = boto3.session.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
        )
    

    # Initialize a session using Boto3
    session = boto3.session.Session()

    # Create an S3 client
    s3 = session.client('s3')
    bucket_name='invest-tracker-dash-app'
    object_key='lamina_fi_rentab_mes_202311.csv'
    # Fetch the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # Read the file content into pandas DataFrame
    file_content = response['Body'].read()
    df = pd.read_csv(BytesIO(file_content), encoding='ISO-8859-1', quoting=csv.QUOTE_NONE, sep=";")

    # df = pd.read_csv("data/if_lamina/lamina_fi_rentab_mes_202311.csv", sep=";", encoding='ISO-8859-1', quoting=csv.QUOTE_NONE)
    df['DT_COMPTC'] = pd.to_datetime(df['DT_COMPTC'], format='%Y-%m-%d')
    df['PR_RENTAB_MES'] = pd.to_numeric(df['PR_RENTAB_MES'], errors='coerce')
    df['PR_VARIACAO_INDICE_REFER_MES'] = pd.to_numeric(df['PR_VARIACAO_INDICE_REFER_MES'], errors='coerce')
    df['PR_PERFM_INDICE_REFER_MES'] = pd.to_numeric(df['PR_PERFM_INDICE_REFER_MES'], errors='coerce')
    cnpj_top_performer = df.loc[df['PR_RENTAB_MES'].idxmax(), 'CNPJ_FUNDO']
    df_filtered = df[df['CNPJ_FUNDO'] != cnpj_top_performer]
    return df_filtered

def simplify_fund_name(name):
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

def prepare_november_data(df):
    # Filtering the dataset for the month of November (MES_RENTAB == 11)
    november_data = df[df['MES_RENTAB'] == 11]

    # Finding the top 5 performing funds in November based on 'PR_RENTAB_MES'
    top_5_november_funds = november_data.nlargest(5, 'PR_RENTAB_MES')['CNPJ_FUNDO'].unique()

    # Filtering the original dataset for the historical data of these top 5 funds
    historical_data_top_5_november = df[df['CNPJ_FUNDO'].isin(top_5_november_funds)]
    historical_data_top_5_november['Year'] = historical_data_top_5_november['DT_COMPTC'].dt.year
    historical_data_top_5_november['Month-Year'] = pd.to_datetime(historical_data_top_5_november['Year'].astype(str) + '-' + historical_data_top_5_november['MES_RENTAB'].astype(str))
    historical_data_top_5_november['Simplified_Name_V2'] = historical_data_top_5_november['DENOM_SOCIAL'].apply(simplify_fund_name)
    return historical_data_top_5_november
# Other data processing functions as needed

# %%
