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

df=df.sample(2)

for i, row in df.iterrows(): 
    #Getting street name only
    PickUp = row["Pick Up"].split(",")[0] 
    DropOff = row['Drop Off'].split(",")[0]


    #Changing given 24 hour time into Epoch Time to match directions api standards
    Time = f"{triplet[2]}".replace(" ", "")
    Time_String = "9 Mar 2020 " + Time
    Striptime = time.strptime(Time_String, "%d %b %Y %H:%M:%S") 
    Time = str(time.mktime(Striptime))[:-2]

    #Changing to directions API url format
    key = "AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw"
    base = "https://maps.googleapis.com/maps/api/directions"
    response = "json"
    data = []

    #Get rid of commas, replace " " with "+", change formatting for outlier location names
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
    
    #json/location data into dict
    if not json_data1.get("error message") 
       or json_data2.get("error message") 
       or json_data3.get("error message"):
        # print(dictionary)
        data.append(dictionary)
    else:
        print("ERROR")

with open("testingjson2.json", "w") as ts: #Copies dictionary info into json
    ts.write(json.dumps(data, indent=2))


    # TODO: remove triplets and replace with itterrows
    # TODO: do the string processing after you've built it (after the if statements, possibyl after url)
    # PickUp = f"{PickUp}".replace(" ", "+").replace(",", "") #Changing format to suit directions api standards
    # DropOff = f"{DropOff}".replace(" ", "+").replace(",", "")



    # if "New South Wales" or "NSW" or "Sydney" in triplet[0]: #Adding on City/State information afterwards
    #     if "Sydney" in triplet[0]:
    #         PickUp = PickUp + "+Sydney+NSW"
    #     else:
    #         PickUp = PickUp + "+NSW"
    # elif "Queensland" or "QLD" or "Brisbane" in triplet[0]:
    #     if "Brisbane" in triplet[0]:
    #         PickUp = PickUp + "+Brisbane+QLD"
    #     else:
    #         PickUp = PickUp + "+QLD"
    # elif "VIC" or "Victoria" or "Melbourne" in triplet[0]:
    #     PickUp = PickUp + "+VIC"
    # else:
    #     None
    # if "New South Wales" or "NSW" or "Sydney" in triplet[1]:
    #     if "Sydney" in triplet[0]:
    #         DropOff = DropOff + "+Sydney+NSW"
    #     else:
    #         DropOff = DropOff + "+NSW"
    # elif "Queensland" or "QLD" or "Brisbane" in triplet[1]:
    #     if "Brisbane" in triplet[1]:
    #         DropOff = DropOff + "+Brisbane+QLD"
    #     else:
    #         DropOff = DropOff + "+QLD"
    # elif "VIC" or "Victoria" or "Melbourne" in triplet[1]:
    #     DropOff = DropOff + "+VIC"
    # else:
    #     None
    # TODO: Check if the if/else statements are needed


# for i, row in df['Drop Off'].iterrows(): 
#     for j in baddies:
#         if row['Drop Off'] == j:
#             df_thing = df['Drop Off'].drop(j, axis = 0)

# for i, row in df['Pick Up'].iterrows():
#         if row['Pick Up'] == j:
#             df_thing = df['Pick Up'].drop(j, axis = 0)
# print (df_thing)

# THE AREA OF THINGS THAT I - PROBABLY - DON'T NEED

# df = df[df["Drop Off"].str.contains(" ", na=False)] #All well-formed addresses are more than one word
# df = df[df["Pick Up"].str.contains(" ", na=False)]
# df['boolean'] = df['Drop Off'].str.isupper() #Are any column values all capitals? 
# df = df[~df.boolean] #If they are, remove them
# df['boolean2'] = df['Pick Up'].str.isupper()
# df = df[~df.boolean2]
# df = df.drop(['Unnamed: 0', 'Trip Comment', 'boolean', 'boolean2'], axis=1)
# df = df.replace('New South Wales', 'NSW', regex = True)
# df = df.replace('Queensland', "QLD", regex = True) #Replace state names with acronyms (redundant because of work in loop later on)
# df = df.replace('Victoria', "VIC", regex = True)
# df = df.replace(', Australia', "", regex = True)
# df.to_excel("preview.xlsx")


# #Converting into triplets (which may have ended up not being needed)
# PickUp_List = df['Pick Up'].tolist() #Converting to lists
# DropOff_List = df['Drop Off'].tolist()
# Time_List = df['time'].tolist()
# Length = len(PickUp_List) #Get length for loop
# Triplets_List = []

# for i in range(Length):
#     List = []
#     List.append(PickUp_List[i]) #loop to make triplets
#     List.append(DropOff_List[i])
#     List.append(Time_List[i])
#     Triplets_List.append(List)



# df_thing = df[[True for x in df["Drop Off"] if x not in baddies]] #or False for x in df["Drop Off"] if x in baddies]] 
# TODO: Figure this out - "ValueError: Item wrong length 180 instead of 195."

# df = [df['Drop Off'].drop(baddies, axis=0) for df['Drop Off'] in df]
# df = df_thing
