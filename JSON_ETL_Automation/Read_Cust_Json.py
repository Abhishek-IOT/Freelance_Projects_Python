import json
import os
import pandas as pd

current_working_dir=os.getcwd() 
with open('Customer.json','r') as file:
    data=json.load(file)
print(data)
df=pd.json_normalize(data)
df.to_csv('my_data.csv',index=False)