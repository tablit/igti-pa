# POC: Validate one investment fund data
# [x] Manually download data and upload to folder 
# [] read csv as pd.DataFrame
# [] find example FI - CNPJ: 68.670.512/0001-07
# %%
import pandas as pd
import csv

pd.set_option('max_colwidth', 800)

# DAILY REPORT
# url: https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202312.zip
daily_report = pd.read_csv("data/if_daily_report/inf_diario_fi_202312.csv",sep=";",encoding='ISO-8859-1')

# captação do dia - CAPT_DIA
# cnpj do fundo - CNPJ_FUNDO 
# data competencia - DT_COMPT
# numero de cotistas - NR_COTST
# resgate do dia - RESG_DIA
# tipo do fundo - TP_FUNDO
# patrimônio líquido - VL_PATRIM_LIQ
# valor da cora - VL_QUOTA
# valor total da carteira - VL_TOTAL

csn_daily_report = daily_report.loc[daily_report['CNPJ_FUNDO']=='68.670.512/0001-07']

# 
# url: https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv
# url_dictionary: https://dados.cvm.gov.br/dados/FI/CAD/META/meta_cad_fi.txt

# cad = pd.read_csv("data/if_cad/cad_fi.csv",sep=";",encoding='ISO-8859-1')

# csn_cad = cad.loc[cad['CNPJ_FUNDO']=='68.670.512/0001-07']

# data de patrimônio líquido menos atualizada que informe diário

# url: https://dados.cvm.gov.br/dados/FI/DOC/LAMINA/DADOS/lamina_fi_202311.zip
# url_dictionary: https://dados.cvm.gov.br/dados/FI/DOC/LAMINA/META/meta_lamina_fi_txt.zip

lamina_202311_quote_parameter = pd.read_csv("data/if_lamina/lamina_fi_202311.csv",sep=";",encoding='ISO-8859-1',quoting=csv.QUOTE_NONE, engine='python')
#%%
lamina_202311 = pd.read_csv("data/if_lamina/lamina_fi_202311.csv",sep=";",encoding='ISO-8859-1')

# csn_lamina_2023_11 = lamina_202311.loc[lamina_202311['CNPJ_FUNDO']=='68.670.512/0001-07']
# 5438
# 5487 2 linhas

# lamina_carteira_202311 = pd.read_csv("data/if_lamina/lamina_fi_carteira_202311.csv",sep=";",encoding='ISO-8859-1')
# csn_lamina_carteira_202311 = lamina_carteira_202311.loc[lamina_carteira_202311['CNPJ_FUNDO']=='68.670.512/0001-07']

# # rentabilidade histórica
lamina_rentab_mes_202311 = pd.read_csv("data/if_lamina/lamina_fi_rentab_mes_202311.csv",sep=";",encoding='ISO-8859-1')
# csn_lamina_rentab_mes_202311 = lamina_rentab_mes_202311.loc[lamina_rentab_mes_202311['CNPJ_FUNDO']=='68.670.512/0001-07']

# # rentabilidade ano
# lamina_rentab_ano_202311 = pd.read_csv("data/if_lamina/lamina_fi_rentab_ano_202311.csv",sep=";",encoding='ISO-8859-1')
# csn_lamina_rentab_ano_202311 = lamina_rentab_ano_202311.loc[lamina_rentab_ano_202311['CNPJ_FUNDO']=='68.670.512/0001-07']
# %%
