
#IMPORTING NECESSARY LIBRARY
import pandas as pd


#READING DATAF AND CONVERTING DATAFRAME
df=pd.read_csv('menu_data.csv')

# TRANSFORMATIONS
df["description"] = df["description"].str.strip().str[:100]
df['title']=df['title'].str.upper()
df['price']=df['price'].round(0)
print(df)

# CLEANED FILE GENERATION
df.to_csv('menu_data_clean.csv',index=0)