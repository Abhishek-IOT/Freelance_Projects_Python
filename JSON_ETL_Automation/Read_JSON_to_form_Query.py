import json
import os



current_working_dir=os.getcwd() 
with open('Query_Parts.json','r') as file:
    data=json.load(file)

query_generation=f"MERGE INTO {data['Query_Merge_Select_Part']['Target_Database']}.{data['Query_Merge_Select_Part']['Target_Schema']}.{data['Query_Merge_Select_Part']['Target_Table']} as A using ("
print(query_generation)



