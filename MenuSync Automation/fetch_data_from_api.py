#Importing Necessary modules
import requests
import pandas as pd

#URL from which we will get the data.
url="https://fakestoreapi.com/products"


response=requests.get(url=url)
print(response)
#CHECKING THE URL IS CORRECT OR NOT.
if response.status_code==200:
    data=response.json()
else :
    print(f"Error fetching data:{response.status_code}")
    exit()
#print(data)

#CREATING DATAFRAMES
df=pd.json_normalize(data)
print(df)
#df=df[["id","title","price","rating.rate"]]
df=df[["id", "title", "description", "price", "category"]]
print(df)

#Saving the dataframe to CSV
df.to_csv("menu_data.csv",index=0)
print("Data has been saved as CSV")



