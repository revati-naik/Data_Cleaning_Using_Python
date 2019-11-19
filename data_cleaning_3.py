import numpy as np 
import pandas as pd 

olympics_df=pd.read_csv('olympics.csv')
print(olympics_df.head())
print('--------------------------------------------------------------------')

#Skip one row and set the header as the first (0-indexed) row
olympics_df=pd.read_csv('olympics.csv',header=1)
print(olympics_df.head())
print('--------------------------------------------------------------------')

#defining a dictionary that maps current column names (keys) to more usable 
#ones (values)
new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
              '03 !': 'Bronze',
              '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
              '03 !.1': 'Bronze.1',
              '? Games': '# Games',
              '01 !.2': 'Gold.2',
              '02 !.2': 'Silver.2',
              '03 !.2': 'Bronze.2'}

olympics_df.rename(columns=new_names, inplace=True)
print(olympics_df.head())
