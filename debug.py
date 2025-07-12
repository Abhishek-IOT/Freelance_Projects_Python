


from datetime import datetime

print(datetime.now())
current_time=datetime.now().strftime('%Y-%m-%d')


file=f'upload_log_{current_time}.txt'

try :
    with open(file,"w") as f:
        f.write("File Created")
except Exception as e:
    print(e)