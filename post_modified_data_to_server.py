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


success_count=0
failure_count=0

api_url="https://httpbin.org/post_1" 

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
                success_count=success_count+1
             
        else :
            msg=msg+f'error occured : {response.status_code} + \n'
            failure_count=failure_count+1

    except Exception as e:
        print(f'Exception : {e}')
    

#print(msg)
with open(file,"w") as f:
    f.write(msg)
    f.write(f"Success Count : {success_count} \n")
    f.write(f"Failure Count : {failure_count}")
    
        



