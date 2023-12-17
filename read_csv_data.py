# POC: Validate one investment fund data
# [x] Manually download data and upload to folder 
# [] read csv as pd.DataFrame
# [] find example FI - CNPJ: 68.670.512/0001-07

import pandas as pd

# url: https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/
daily_report = pd.read_csv("data/if_daily_report/202312/inf_diario_fi_202312.csv",sep=";")

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