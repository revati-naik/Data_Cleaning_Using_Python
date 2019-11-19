import pandas as pd
import numpy as np

university_towns=[]
with open('university_towns.txt') as file:
	for line in file:
		if '[edit]' in line:
			#remember the state until the next is found
			state=line
		else:
			#otherwise we have a city, keep the state as last seen
			university_towns.append((state,line))

print(university_towns[:5])
print('--------------------------------------------------------------------')

#wrapping the dataframe in tabular form
towns_df=pd.DataFrame(university_towns, columns=['State','RegionName'])
print(towns_df.head())
print('--------------------------------------------------------------------')

#more cleaning of data using applymap()
def get_citystate(item):
	if '(' in item:
		return item[:item.find(' (')]
	elif '[' in item:
		return item[:item.find('[')]
	else:
		return item
towns_df=towns_df.applymap(get_citystate)
print(towns_df.head())