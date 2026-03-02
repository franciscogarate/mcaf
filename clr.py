import pandas as pd

file = ('./mcaf/data/EIOPA_RFR_20251231_Term_Structures.xlsx')
rfr = pd.read_excel(file, sheet_name='RFR_spot_no_VA', skiprows=9, usecols=(1,2), names=['t','Euro'])
clr = rfr['Euro'].loc[:150].tolist()
