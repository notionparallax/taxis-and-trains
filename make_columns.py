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
data = []

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


with open('samplejson(10).json') as f:
    data = f.read()
    data2 = json.loads(data)

    row_count = len(data2)
    step_count = (len(data2[5]['Transit']['routes'][0]['legs'][0]['steps'][0]['steps']))
    print(data2[5]['Transit']['routes'][0]['legs'][0]['steps'][1]['transit_details']['line']['vehicle']['type'])
    # print(data2[5]['Transit']['routes'][0]['legs'][0]['steps'])

    # for i in range(0, int(step_count)):
    #     print(data2[5]['Transit']['routes'][0]['legs'][0]['steps'][0]['steps'][i]['travel_mode'])



"""
#Walking Information
    main_list_start = []
    main_list_end = []
    for i in range(0, int(row_count)):
        sublist_start = []
        sublist_end = []
        d = data2[i]
        start_lat = d['Walking']['routes'][0]['legs'][0]['start_location']['lat']
        start_lng = d['Walking']['routes'][0]['legs'][0]['start_location']['lng']
        end_lat = d['Walking']['routes'][0]['legs'][0]['end_location']['lat']
        end_lng = d['Walking']['routes'][0]['legs'][0]['end_location']['lng']
        sublist_start.append(start_lat)
        sublist_start.append(start_lng)
        sublist_end.append(end_lat)
        sublist_end.append(end_lng)
        main_list_start.append(sublist_start)
        main_list_end.append(sublist_end)
    df['Walking Start Lat and Long'] = main_list_start
    df['Walking End Lat and Long'] = main_list_end

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        time = d['Walking']['routes'][0]['legs'][0]['duration']['text']
        main_list.append(time)
    df['Walking Time'] = main_list

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        dis = d['Walking']['routes'][0]['legs'][0]['distance']['text']
        main_list.append(dis)
    df['Walking Distance'] = main_list



#Driving Information
    main_list_start = []
    main_list_end = []
    for i in range(0, int(row_count)):
        sublist_start = []
        sublist_end = []
        d = data2[i]
        start_lat = d['Driving']['routes'][0]['legs'][0]['start_location']['lat']
        start_lng = d['Driving']['routes'][0]['legs'][0]['start_location']['lng']
        end_lat = d['Driving']['routes'][0]['legs'][0]['end_location']['lat']
        end_lng = d['Driving']['routes'][0]['legs'][0]['end_location']['lng']
        sublist_start.append(start_lat)
        sublist_start.append(start_lng)
        sublist_end.append(end_lat)
        sublist_end.append(end_lng)
        main_list_start.append(sublist_start)
        main_list_end.append(sublist_end)
    df['Driving Start Lat and Long'] = main_list_start
    df['Driving End Lat and Long'] = main_list_end

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        time = d['Driving']['routes'][0]['legs'][0]['duration']['text']
        main_list.append(time)
    df['Driving Time'] = main_list

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        dis = d['Driving']['routes'][0]['legs'][0]['distance']['text']
        main_list.append(dis)
    df['Driving Distance'] = main_list



    main_list_start = []
    main_list_end = []
    for i in range(0, int(row_count)):
        sublist_start = []
        sublist_end = []
        d = data2[i]
        try:
            start_lat = d['Transit']['routes'][0]['legs'][0]['start_location']['lat']
            start_lng = d['Transit']['routes'][0]['legs'][0]['start_location']['lng']
            end_lat = d['Transit']['routes'][0]['legs'][0]['end_location']['lat']
            end_lng = d['Transit']['routes'][0]['legs'][0]['end_location']['lng']
            sublist_start.append(start_lat)
            sublist_start.append(start_lng)
            sublist_end.append(end_lat)
            sublist_end.append(end_lng)
            main_list_start.append(sublist_start)
            main_list_end.append(sublist_end)
        except:
            main_list_start.append("Transit Unavailable")
            main_list_end.append("Transit Unavailable")
    df['Transit Start Lat and Long'] = main_list_start
    df['Transit End Lat and Long'] = main_list_end

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        try:
            time = d['Transit']['routes'][0]['legs'][0]['duration']['text']
            main_list.append(time)
        except: 
            main_list.append("Transit Unavailable")
    df['Transit Time'] = main_list

    main_list = []
    for i in range(0, int(row_count)):
        d = data2[i]
        try:
            time = d['Transit']['routes'][0]['legs'][0]['distance']['text']
            main_list.append(time)
        except: 
            main_list.append("Transit Unavailable")
    df['Transit Distance'] = main_list"""









# TODO: Is there a way to accomplish what I am doing with the functions and the apply, but as a single function/apply?
#     def Walk_Start_Lat(row):
#         for i in range (1):

#     def Walk_Start_Lng(row):

#     def Walk_End_Lat(row):

#     def Walk_End_Lng(row):

#     def Walk_Time(row):

#     def Walk_Distance(row):

#     def Driv_Start_Lat(row):
        
#     def Driv_Start_Lng(row):

#     def Driv_End_Lat(row):

#     def Driv_End_Lng(row):

#     def Driv_Time_Taken(row):

#     def Driv_Distance(row):

#     def Tran_Start_Lat(row):
        
#     def Tran_Start_Lng(row):

#     def Tran_End_Lat(row):

#     def Tran_End_Lng(row):

#     def Tran_Time_Taken(row):

#     def Tran_Distance(row):

#     def Tran_Mode(row):

#     data2['Walking Start Latitude'] = data2.apply(Walk_Start_Lat, axis=1)

# print (data2.sample(10))

# print("given pick up location", d['Pick Up'])    
# print("given drop off location", d['Drop Off'])    
# print("given 24hr time", d['Time'])

# print("Walking")
# print("start latitude", d['Walking']['routes'][0]['legs'][0]['start_location']['lat'])
# print("start longitude", d['Walking']['routes'][0]['legs'][0]['start_location']['lng'])
# print("end latitude", d['Walking']['routes'][0]['legs'][0]['end_location']['lat'])
# print("end longitude", d['Walking']['routes'][0]['legs'][0]['end_location']['lng'])

# print("Walking total time taken", d['Walking']['routes'][0]['legs'][0]['duration']['text'])
# print("Walking total distance travelled", d['Walking']['routes'][0]['legs'][0]['distance']['text'])

# print("Driving")
# print("Driving total time taken", d['Driving']['routes'][0]['legs'][0]['duration']['text'])
# print("Driving total distance travelled", d['Driving']['routes'][0]['legs'][0]['distance']['text'])

# print("Transit total time taken", d['Transit']['routes'][0]['legs'][0]['duration']['text'])
# print("Transit total distance travelled", d['Transit']['routes'][0]['legs'][0]['distance']['text'])

# print(d['Transit'])



#mode for each leg in journey
#apply = pandas 1.0 feat - multi column response - in df.apply docs (you'll get a new df and you'll have to merge it with the old one) 
# --> get new df, make it into excel sheet, do it for a sample of 10
# result_type: "expand" 
#query on the json object and find which one it is 
# if the drop off and the pick up and the time all match then 
# thisItem = [item for item in my_list if item['pickup'] == row.pickup and item['dropoff'] == row.dropoff and item['pickup'] == "here" and item["time"] == "now"][0] 
#'there' 'here', etc from the row in pandas df, use the above for multi column apply - result-type expand (see above)

# for i in range(0, row_count-1):

# demo_route(0, "Pitt St to Bourke St")    
# demo_route(1, "Park St to Pacific Hwy")    
 
# Walking Data
