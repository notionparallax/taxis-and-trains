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

df = df.head(10)


with open('samplejson(10).json') as f:
    data = f.read()
    data2 = json.loads(data)

    # Find number of items in data2
    row_count = int(len(data2))

# Walking Information
    # Create main lists for later appending
    main_list_start = []
    main_list_end = []
    for i in range(0, row_count):
        # Create sublists for start and end coordinates (each row gets a new sublist)
        sublist_start = []
        sublist_end = []
        # Re-designating "data2[i]" to step through the loop
        d = data2[i]
        # Pathways to dict information
        start_lat = d['Walking']['routes'][0]['legs'][0]['start_location']['lat']
        start_lng = d['Walking']['routes'][0]['legs'][0]['start_location']['lng']
        end_lat = d['Walking']['routes'][0]['legs'][0]['end_location']['lat']
        end_lng = d['Walking']['routes'][0]['legs'][0]['end_location']['lng']
        # Append information to smaller sublists
        sublist_start.append(start_lat)
        sublist_start.append(start_lng)
        sublist_end.append(end_lat)
        sublist_end.append(end_lng)
        # Append the information for that row to the main_list and reset for the next iterration
        main_list_start.append(sublist_start)
        main_list_end.append(sublist_end)
    # Add new columns to original df
    df['Walking Start Lat and Long'] = main_list_start
    df['Walking End Lat and Long'] = main_list_end

    # Reset main list each time so that the new values aren't appended to the old
    main_list = []
    for i in range(0, row_count):
        d = data2[i]
        time = d['Walking']['routes'][0]['legs'][0]['duration']['text']
        main_list.append(time)
    df['Walking Time'] = main_list

    main_list = []
    for i in range(0, row_count):
        d = data2[i]
        dis = d['Walking']['routes'][0]['legs'][0]['distance']['text']
        main_list.append(dis)
    df['Walking Distance'] = main_list



#Driving Information
    main_list_start = []
    main_list_end = []
    for i in range(0, row_count):
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
    for i in range(0, row_count):
        d = data2[i]
        time = d['Driving']['routes'][0]['legs'][0]['duration']['text']
        main_list.append(time)
    df['Driving Time'] = main_list

    main_list = []
    for i in range(0, row_count):
        d = data2[i]
        dis = d['Driving']['routes'][0]['legs'][0]['distance']['text']
        main_list.append(dis)
    df['Driving Distance'] = main_list


# Transit Information
# Not all routes have a transit option, hence the try/except
    main_list_start = []
    main_list_end = []
    for i in range(0, row_count):
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
    for i in range(0, row_count):
        d = data2[i]
        try:
            time = d['Transit']['routes'][0]['legs'][0]['duration']['text']
            main_list.append(time)
        except: 
            main_list.append("Transit Unavailable")
    df['Transit Time'] = main_list

    main_list = []
    for i in range(0, row_count):
        d = data2[i]
        try:
            time = d['Transit']['routes'][0]['legs'][0]['distance']['text']
            main_list.append(time)
        except: 
            main_list.append("Transit Unavailable")
            print(d['Pick Up'])
            print(d['Drop Off'])
    df['Transit Distance'] = main_list  
    
    main_list = []
    for i in range(0, row_count):
        try:
            sublist1 = []
            step1_count = int(len(data2[i]['Transit']['routes'][0]['legs'][0]['steps']))
            for j in range(0, step1_count):
                sublist2 = []
                try:
                    mode = (data2[i]['Transit']['routes'][0]['legs'][0]['steps'][j]['steps'][0]['travel_mode'])
                    sublist1.append(mode)
                except:   
                    mode = (data2[i]['Transit']['routes'][0]['legs'][0]['steps'][j]['transit_details']['line']['vehicle']['type'])
                    sublist1.append(mode)
        except:
            sublist1.append("Transit Unavailable")
        main_list.append(sublist1)
    df['Transit Mode'] = main_list

    # df.to_excel(writer, sheet_name = "make_columns1") 

