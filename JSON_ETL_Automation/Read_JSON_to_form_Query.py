import json
import os



current_working_dir=os.getcwd() 
with open('Query_Parts.json','r') as file:
    data=json.load(file)

query_generation=f"MERGE INTO {data['Query_Merge_Select_Part']['Target_Database']}.{data['Query_Merge_Select_Part']['Target_Schema']}.{data['Query_Merge_Select_Part']['Target_Table']} as A using ("
print(query_generation)

select_clauses=[]

for col in data['ETL_Logic']['Columns']:
    clause = f"{col['Source_Table_Name']}.{col['Logic']} AS {col['Target_Column_Name']}"
    select_clauses.append(clause)

select_statement = "SELECT " + ",\n       ".join(select_clauses)
select_statement=select_statement+ " FROM " +f'{data['Query_Merge_Select_Part']['Source_Table']}'
print(select_statement)

joiner_clause=[]
for col in data['Joiner']:
    clause=f"{col['type']}  JOIN {col['joiner_table']} ON {col['Condition']}"
    #print(clause)
    joiner_clause.append(clause)
#print(joiner_clause)
join_statement = "\n       ".join(joiner_clause)
print(join_statement)

filter_statement=f'where {data['Filter_Conditions']['Condition']}'
print(filter_statement)


