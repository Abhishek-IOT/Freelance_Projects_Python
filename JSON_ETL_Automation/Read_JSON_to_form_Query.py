import json
import os



current_working_dir=os.getcwd() 
with open('Query_Parts.json','r') as file:
    data=json.load(file)

query_generation=f"MERGE INTO {data['Query_Merge_Select_Part']['Target_Database']}.{data['Query_Merge_Select_Part']['Target_Schema']}.{data['Query_Merge_Select_Part']['Target_Table']} as A using ("
print(query_generation)

select_clauses=[]

for col in data['ETL_Logic']['Columns']:
    clause = f"{col['Source_Column_Name']}.{col['Logic']} AS {col['Target_Column_Name']}"
    select_clauses.append(clause)

select_statement = "SELECT " + ",\n       ".join(select_clauses)
print(select_statement)

