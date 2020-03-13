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

baddies = [
    "AIRPORT",
    "CITY",
    "CRONULLA",
    "Freshwater",
    "Greenwich",
    "HOME",
    "Mascot",
    "OFFICE",
    "SUBURBS",
    # "SYD DOM ARPT",
    # "SYD INT ARPT"
    "Strathfield",
    "Sydney CBD",
    "Sydney CBD, New South Wales, 2000",
    "Sydney",
    # "TOWN HALL",
]

#Cleaning Dataset
df = df[pd.notnull(df['Drop Off'])] #remove null values
df = df[pd.notnull(df['Pick Up'])]

df = df[~df['Pick Up'].isin(baddies)] #If baddies items are in "Pick Up" column, remove their row
df = df[~df['Drop Off'].isin(baddies)] #If baddies items are in "Drop Off" column, remove their row

df = df.sample(10)

for i, row in df.iterrows(): 
    #Getting street name only
    PickUp = row["Pick Up"].split(",")[0] 
    DropOff = row["Drop Off"].split(",")[0]

    #Changing given 24 hour time into Epoch Time to match directions api standards
    Time = row['Time'].replace(" ", "")
    Time_String = "9 Mar 2020 " + Time
    Striptime = time.strptime(Time_String, "%d %b %Y %H:%M:%S") 
    Time = str(time.mktime(Striptime))[:-2]

    #Changing to directions API url format
    key = "AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw"
    base = "https://maps.googleapis.com/maps/api/directions"
    response = "json"
    data = []

    #Getting rid of commas, replace " " with "+", change formatting for outlier location names
    dir_url_walking = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"walking"+"&arrival_time="+Time 
    dir_url_walking = dir_url_walking.replace('TOWN HALL', 'Town Hall Sydney NSW').replace('SYD INT ARPT', 'Sydney International Airport').replace('SYD DOM ARPT', "Sydney Domestic Airport").replace(" ", "+").replace(",", "")

    dir_url_driving = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"driving"+"&arrival_time="+Time
    dir_url_driving = dir_url_driving.replace('TOWN HALL', 'Town Hall Sydney NSW').replace('SYD INT ARPT', 'Sydney International Airport').replace('SYD DOM ARPT', "Sydney Domestic Airport").replace(" ", "+").replace(",", "")

    dir_url_transit = f"{base}/{response}?origin="+PickUp+"&destination="+DropOff+"&key="+key+"&mode="+"transit"+"&arrival_time="+Time
    dir_url_transit = dir_url_transit.replace('TOWN HALL', 'Town Hall Sydney NSW').replace('SYD INT ARPT', 'Sydney International Airport').replace('SYD DOM ARPT', "Sydney Domestic Airport").replace(" ", "+").replace(",", "")

    #Request and store API data
    r_walking = requests.get(dir_url_walking)
    r_driving = requests.get(dir_url_driving)
    r_transit = requests.get(dir_url_transit)

    json_data_walking=r_walking.json()
    json_data_driving=r_driving.json()
    json_data_transit=r_transit.json()
    
    dictionary = {
        "Pick Up":row['Pick Up'], 
        "Drop Off":row['Drop Off'], 
        "Time":row['Time'], 
        "Walking":json_data_walking, 
        "Driving":json_data_driving, 
        "Transit":json_data_transit
    }
    
    #\json/location data into dict
    if not json_data_walking.get("error message") or json_data_driving.get("error message") or json_data_transit.get("error message"):
        # print(dictionary)
        data.append(dictionary)
    else:
        print("ERROR")

with open("samplejson(10).json", "w") as ts: #Copies dictionary info into json
    ts.write(json.dumps(dictionary, indent=2))