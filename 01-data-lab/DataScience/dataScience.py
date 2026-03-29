# %%
4 + 2
# %%
import numpy as np
import pandas as pd

# creating a dataframe from a series and using a list of column heads as index
# regional info
regional_info = ['schools', 'regions', 'regional_capitals', 'IGF_Ghs']

# regions
regions = pd.Series(['northern', 'volta', 'greater accra',
            'eastern', 'upper east', 'bono', 'oti',
            'upper west'])
# schools
schools = pd.Series(['tamasco', 'anseco', 'accra academy', 'adonten',
           'navrosec', 'aburi girls', 'ketesec', 'wasec'])
#regional capital 
regional_capitals = pd.Series(['tamale', 'ho', 'accra', 'koforidua',
                     'bolga', 'sunyani', 'ketekrachi', 'wa'])
# Internally Generated Fund(GHS)
IGF_Ghs = pd.Series([500603, 66890, 3000567, 88933, 90778, 70098, 904789, 455876])

# Generating a DataFrame
df = pd.DataFrame([schools, regions, regional_capitals, IGF_Ghs], 
                  index=regional_info)
print(df.T)
print(df)
# %%
print(df.describe())
print(df.info())
print(df.isnull().sum())
# %%
