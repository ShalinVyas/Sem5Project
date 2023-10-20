from datetime import datetime, timedelta
import pandas as pd

data = pd.read_csv("./abc.csv")
df = pd.DataFrame(data)
#print(df)
#df['Date'] = pd.to_datetime(df['Time Created'])

#df['Time'] = pd.to_datetime(df['Time']).dt.time

df['Time'] = [d.time() for d in df['Time']]
print(df['Time'])
current_event = None
result = []
for event, time in zip(df['Source'], df['Time']):
    if event != current_event:
        if current_event is not None:
            result.append([current_event, start_time, time])
        current_event, start_time = event, time
data1 = pd.DataFrame(result, columns=['Event','EventStartTime','EventEndTime'])
data1.to_csv("output.csv",index=False)
print(df)
