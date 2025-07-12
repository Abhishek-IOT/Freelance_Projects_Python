#IMPORTING THE NECESSARY LIBRARY
import pandas as pd
import requests
import time

#CREATING DATAFRAME FROM CSV DATA.
df=pd.read_csv('Menu_data.csv')

api_url="https://httpbin.org/post" 

for _,row in df.iterrows():
    load={
        "id":row["id"],
        "Title":row["title"],
        "description":row["description"],
        "price":row["price"],
        "category":row["category"]
    }
    
    try:
        response=requests.post(api_url,json=load)
        if response.status_code==200:
            print(f'Uploaded:{row['title']}')
        else :
            print(f'error occured : {response.status_code}')
    except Exception as e:
        print(f'Exception : {e}')
    
    
        



