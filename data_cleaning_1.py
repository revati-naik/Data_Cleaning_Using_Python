import pandas as pd
import numpy as np 

#reading the dataset in csv format (first 5 entries)
df=pd.read_csv('BL-Flickr-Images-Book.csv')
print('Read first 5 entries of the dataset')
print(df.head())
print('--------------------------------------------------------------------')


#drop unwanted columns
to_drop=['Edition Statement','Corporate Contributors','Former owner','Engraver',
		'Contributors','Issuance type','Shelfmarks']
print('Drop unwanted columns')
print(df.drop(to_drop, inplace=True, axis=1))
print('--------------------------------------------------------------------')


#changing the index of a dataframe
df=df.set_index('Identifier')
print('Change the index to Indentifier')
print(df.head())
print('--------------------------------------------------------------------')

#clean specific columns and get them to uniform format 
#playing with the Date of Publication field
print('Cleaning the Date of Publication column')
print(df.loc[1905:,'Date of Publication'].head(10))
print('--------------------------------------------------------------------')

#eliminating garbage values of years
print('Correctly displaying the year')
year_change=df['Date of Publication'].str.extract(r'^(\d{4})',expand=False)
print(year_change.head())
print('--------------------------------------------------------------------')

#converting Date of Publication to dtype=numeric
df['Date of Publication']=pd.to_numeric(year_change)
print('Changing Dtype of year to float')
print(df['Date of Publication'].dtype)
print('--------------------------------------------------------------------')

#Combining str Methods with NumPy to Clean Columns

#read the first 10 entries in the Place of Publication field
print('Place of Publication field')
print(df['Place of Publication'].head(10))
print('--------------------------------------------------------------------')

#cleaning unwanted names in the field
single_name=df['Place of Publication']
london=single_name.str.contains('London')
oxford=single_name.str.contains('Oxford')

#using np.where() to combine the two logics
df['Place of Publication']=np.where(london, 'London',np.where(oxford,'Oxford',
	single_name.str.replace('-',' ')))
print('Cleaned Place of Publication field')
print(df['Place of Publication'].head())
print('--------------------------------------------------------------------')
