#IMPORTING THE NECESSARY LIBRARY
import pandas as pd
import requests
import time
from datetime import datetime

#CREATING DATAFRAME FROM CSV DATA.
df=pd.read_csv('Menu_data.csv')


##DYNMAMIC LOG FILE CREATED
current_time=datetime.now().strftime('%Y-%m-%d')


file=f'upload_log_{current_time}.txt'




api_url="https://httpbin.org/post" 

msg=''
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
                msg=msg+f'Uploaded:{row['title']}'+'\n'
             
        else :
            msg=print(f'error occured : {response.status_code}')
    except Exception as e:
        print(f'Exception : {e}')
    
print(msg)
with open(file,"w") as f:
    f.write(msg)

    
        



