from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import pandas as pd
import json
import requests
import time

path = "in"
df = pd.read_excel(os.path.join(path, "200taxis.xlsx"))


#Cleaning Dataset
df = df[pd.notnull(df['Drop Off'])]
df = df[pd.notnull(df['Pick Up'])]
df = df[df["Drop Off"].str.contains(" ", na=False)]
df = df[df["Pick Up"].str.contains(" ", na=False)]
df['boolean'] = df['Drop Off'].str.isupper() #Are any column values all capitals?
df = df[~df.boolean] #If they are, remove them
df['boolean2'] = df['Pick Up'].str.isupper()
df = df[~df.boolean2]
df = df.drop(['Unnamed: 0', 'Trip Comment', 'boolean', 'boolean2'], axis=1)
# df = df.replace('New South Wales', 'NSW', regex = True)
# df = df.replace('Queensland', "QLD", regex = True) #Replace state names with acronyms (redundant because of work in loop later on)
# df = df.replace('Victoria', "VIC", regex = True)
# df = df.replace(', Australia', "", regex = True)
df=df.sample(2)


#Converting into triplets (which may have ended up not being needed)
PickUp_List = df['Pick Up'].tolist() #Converting to lists
DropOff_List = df['Drop Off'].tolist()
Time_List = df['time'].tolist()
Length = len(PickUp_List) #Get length for loop
Triplets_List = []

for i in range(Length):
    List = []
    List.append(PickUp_List[i]) #loop to make triplets
    List.append(DropOff_List[i])
    List.append(Time_List[i])
    Triplets_List.append(List)

#Converting to json

key = "AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw"
base = "https://maps.googleapis.com/maps/api/directions"
response = "json"
data = []
for triplet in Triplets_List:
    PickUp = triplet[0].split(",")[0] #Getting Street Name
    PickUp = f"{PickUp}".replace(" ", "+").replace(",", "") #Changing format to suit directions api standards
    DropOff = triplet[1].split(",")[0]
    DropOff = f"{DropOff}".replace(" ", "+").replace(",", "")
    if "New South Wales" or "NSW" or "Sydney" in triplet[0]: #Adding on City/State information afterwards
        if "Sydney" in triplet[0]:
            PickUp = PickUp + "+Sydney+NSW"
        else:
            PickUp = PickUp + "+NSW"
    elif "Queensland" or "QLD" or "Brisbane" in triplet[0]:
        if "Brisbane" in triplet[0]:
            PickUp = PickUp + "+Brisbane+QLD"
        else:
            PickUp = PickUp + "+QLD"
    elif "VIC" or "Victoria" or "Melbourne" in triplet[0]:
        PickUp = PickUp + "+VIC"
    else:
        None
    if "New South Wales" or "NSW" or "Sydney" in triplet[1]:
        if "Sydney" in triplet[0]:
            DropOff = DropOff + "+Sydney+NSW"
        else:
            DropOff = DropOff + "+NSW"
    elif "Queensland" or "QLD" or "Brisbane" in triplet[1]:
        if "Brisbane" in triplet[1]:
            DropOff = DropOff + "+Brisbane+QLD"
        else:
            DropOff = DropOff + "+QLD"
    elif "VIC" or "Victoria" or "Melbourne" in triplet[1]:
        DropOff = DropOff + "+VIC"
    else:
        None
    Time = f"{triplet[2]}".replace(" ", "")
    Time_String = "9 Mar 2020 " + Time
    Striptime = time.strptime(Time_String, "%d %b %Y %H:%M:%S") #Changing given 24 hour time into Epoch Time to match directions api standards
    Time = str(time.mktime(Striptime))[:-2]
    dir_url1 = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"walking"+"&arrival_time="+Time #Need way to combine into 1 request
    dir_url2 = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"driving"+"&arrival_time="+Time
    dir_url3 = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"transit"+"&arrival_time="+Time
    r1 = requests.get(dir_url1)#Requests/stores info from directions api
    r2 = requests.get(dir_url2)
    r3 = requests.get(dir_url3)
    json_data1=r1.json()#Stores api info as json
    json_data2=r2.json()
    json_data3=r3.json()
    dictionary = {"Pick Up":triplet[0], "Drop Off":triplet[1], "Time":triplet[2], "Walking":json_data1, "Driving":json_data2, "Public Transport":json_data3}#json/location data into dict
    if not json_data1.get("error message") or json_data2.get("error message") or json_data3.get("error message"):
        # print(dictionary)
        data.append(dictionary)
    else:
        print("ERROR")

with open("testingjson2.json", "w") as ts: #Copies dictionary info into json
    ts.write(json.dumps(data, indent=2))







    # if not json_data.get("error_message"):
    #     data.append(json_data)
    # else:
    #     json_data["url"] = geo_url
    #     json_data["name"] = name
    #     data.append({json_data})    
    # else:
    #     json_data1

    # for name in problem_station_names:
    # address = f"{name} Train Station, NSW".replace(" ", "+")
    # geo_url = f"{base}/{response}?address={address}&key={key}"
    # # print(geo_url)
    # r = requests.get(geo_url)
    # json_data = r.json()




    # print(dictionary)






# with open("testingjson.json", "w") as ts:
#     ts.write(json.dumps(dictionary))

    # print(dictionary)

    # json_data_walk = r1.json()
    # json_data_drive = r2.json()
    # json_data_transit = r3.json()


    #dictionary = {triplet : }
    # print(dir_url)
    # r = requests.get(dir_url)
    # json_data = r.json()
    # if not json_data.get("error_message"):
    #     data.append(json_data)
    # else:
    #     json_data["url"] = dir_url
    #     data.append({json_data})





# print(data)


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

# df = df['Drop Off'].str.slice(0, -5)
# df[0].str.slice(0, -5)
# print(df.columns.tolist())
# dfsample = df["Drop Off"].sample(60)
# print(dfsample)
# dfsample = df["Pick Up"].sample(60)
# print(dfsample)
