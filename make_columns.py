from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import pandas as pd
import json
import requests
import time

with open('samplejson(10).json') as f:
    data = f.read()
    data2 = json.loads(data)

    row_count = len(data2)

# Pitt St to Underwood St
# Walking Data
# def demo_route(index, description):
d = data2[0]
# print(d)

print("given pick up location", d['Pick Up'])    
print("given drop off location", d['Drop Off'])    
print("given 24hr time", d['Time'])

print("Walking")
print("start latitude", d['Walking']['routes'][0]['legs'][0]['start_location']['lat'])
print("start longitude", d['Walking']['routes'][0]['legs'][0]['start_location']['lng'])
print("end latitude", d['Walking']['routes'][0]['legs'][0]['end_location']['lat'])
print("end longitude", d['Walking']['routes'][0]['legs'][0]['end_location']['lng'])

print("Walking total time taken", d['Walking']['routes'][0]['legs'][0]['duration']['text'])
print("Walking total distance travelled", d['Walking']['routes'][0]['legs'][0]['distance']['text'])

print("Driving")
print("Driving total time taken", d['Driving']['routes'][0]['legs'][0]['duration']['text'])
print("Driving total distance travelled", d['Driving']['routes'][0]['legs'][0]['distance']['text'])

print("Transit total time taken", d['Transit']['routes'][0]['legs'][0]['duration']['text'])
print("Transit total distance travelled", d['Transit']['routes'][0]['legs'][0]['distance']['text'])

print(d['Transit'])


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
