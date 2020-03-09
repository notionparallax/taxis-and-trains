from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import pandas as pd
import json
import requests

path = "in"
df = pd.read_excel(os.path.join(path, "200taxis.xlsx"))


#Cleaning Dataset
df = df[pd.notnull(df['Drop Off'])]
df = df[pd.notnull(df['Pick Up'])]
df = df[df["Drop Off"].str.contains(" ", na=False)]
df = df[df["Pick Up"].str.contains(" ", na=False)]
df['boolean'] = df['Drop Off'].str.isupper() 
df = df[~df.boolean]
df['boolean2'] = df['Pick Up'].str.isupper()
df = df[~df.boolean2]
df = df.drop(['Unnamed: 0', 'Trip Comment', 'boolean', 'boolean2'], axis=1)


#Converting into triplets (which may have ended up not being needed)
PickUp_List = df['Pick Up'].tolist() 
DropOff_List = df['Drop Off'].tolist()
Time_List = df['time'].tolist()
Length = len(PickUp_List)
Triplets_List = []

for i in range(Length):
    List = []
    List.append(PickUp_List[i])
    List.append(DropOff_List[i])
    List.append(Time_List[i])
    Triplets_List.append(List)


#Converting to json
#For json file: Startpoint/endpoint as key, 3 responses of walking, driving and public transport 

key = "AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw"
base = "https://maps.googleapis.com/maps/api/directions/"
response = "json"
data = []
for triplet in Triplets_List:
    PickUp = f"{triplet[0]}".replace(" ", "+").replace(",", "")
    DropOff = f"{triplet[1]}".replace(" ", "+").replace(",", "")
    Time = f"{triplet[2]}".replace(" ", "")
    dir_url = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key=____"+"&mode=_____"+"&arrival_time="+Time
    data.append(dir_url)
    print(dir_url)

#     r = requests.get(dir_url)
#     json_data = r.json()
#     if not json_data.get("error_message"):
#         data.append(json_data)
#     else:
#         json_data["url"] = dir_url
#         data.append({json_data})


# with open("jsondata.json", "w") as ts:
#     ts.write(json.dumps(data, indent=2))


print(data)


    # print(dir_url)





#https://maps.googleapis.com/maps/api/directions/outputFormat?parameters
#https://maps.googleapis.com/maps/api/directions/json?origin=fullstack+academy+ny&destination=penn+station&key=___&mode=___&departure_time=23:58





#     key = "AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw"
# base = "https://maps.googleapis.com/maps/api/geocode"
# print(data)
#     address = f""
#     address = f"{name} Train Station, NSW".replace(" ", "+")
#     dir_url = f"{base}/{response}?address={address}&key={key}"
#     r = requests.get(dir_url)
#     json_data = r.json()
#     if not json_data.get("error_message"):
#         data.append(json_data)
#     else:
#         json_data["url"] = dir_url
#         json_data["name"] = name
#         data.append({json_data})


# with open("jsondata.json", "w") as ts:
#     ts.write(json.dumps(data, indent=2))





# for name in List:
#     address = f"{name} Train Station, NSW".replace(" ", "+")
#     f(List, Lis)

# df = df[df['Drop Off'].str.isupper((), na=False)]
# df['DropOff_isupper'] = map(lambda x: x.isupper(), df['Drop Off'])
# boolean = map(lambda x: x.isupper(), df['Pick Up'])
# df.drop(df[boolean].index, inplace=True)
#df = df[[x.isupper() for x in df['Drop Off'].values]]
#df = df[x[0].isupper() for x in df['EntityName']]
#df = df.drop(["Sydney CBD"], axis=0)
# print(df['Drop Off'].iloc[70:85])
# print(df['Drop Off'])
# print(df['DropOff_isupper'].sample(50))
# print(df['Pick Up'])
# print(boolean.iloc[70:85])