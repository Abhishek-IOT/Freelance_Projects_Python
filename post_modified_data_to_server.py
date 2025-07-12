#IMPORTING THE NECESSARY LIBRARY
import pandas as pd
import requests
import time

#CREATING DATAFRAME FROM CSV DATA.
df=pd.read_csv('Menu_data.csv')


log_file=open("upload_log.txt","a")

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
log_file.write(msg)
    
        



