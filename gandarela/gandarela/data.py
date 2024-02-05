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
from io import BytesIO

from services.aws_utils import get_s3_session, get_data_from_s3


bucket_name='invest-tracker-dash-app'
lamina_file='lamina_fi_rentab_mes_202311.csv'
cad_file='cad_fi.csv'
s3 = get_s3_session()


def load_data():
    
    # Fetch lamina file from S3
    lamina = get_data_from_s3(s3, bucket_name, lamina_file)
    # Process lamina content
    lamina = pd.read_csv(BytesIO(lamina), encoding='ISO-8859-1', quoting=csv.QUOTE_NONE, sep=";")
    lamina['DT_COMPTC'] = pd.to_datetime(lamina['DT_COMPTC'], format='%Y-%m-%d')
    lamina['PR_RENTAB_MES'] = pd.to_numeric(lamina['PR_RENTAB_MES'], errors='coerce')
    lamina['PR_VARIACAO_INDICE_REFER_MES'] = pd.to_numeric(lamina['PR_VARIACAO_INDICE_REFER_MES'], errors='coerce')
    lamina['PR_PERFM_INDICE_REFER_MES'] = pd.to_numeric(lamina['PR_PERFM_INDICE_REFER_MES'], errors='coerce')
    
    cad = get_data_from_s3(s3, bucket_name, cad_file)
    cad = pd.read_csv(BytesIO(cad), encoding='ISO-8859-1', quoting=csv.QUOTE_NONE, sep=";")
    
    return lamina, cad

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

def prepare_data_for_performance_graph(df):
    prepared_data = df.copy()
    prepared_data['Year'] = prepared_data['DT_COMPTC'].dt.year
    prepared_data['Month-Year'] = pd.to_datetime(prepared_data['Year'].astype(str) + '-' + prepared_data['MES_RENTAB'].astype(str))
    prepared_data['Simplified_Name_V2'] = prepared_data['DENOM_SOCIAL'].apply(simplify_fund_name)
    return prepared_data
# Other data processing functions as needed

# %%
