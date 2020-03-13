from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import pandas as pd
import json
import requests
import time

with open('testingjson2.json') as f:
    data = f.read()
    data2 = json.loads(data)
# Pitt St to Underwood St
# Walking Data
    info = data2[0]['Pick Up'] #given pick up location
    info = data2[0]['Drop Off'] #given drop off location
    info = data2[0]['Time'] #given 24hr time

    info = data2[0]['Walking']['routes'][0]['legs'][0]['start_location']['lat'] # start latitude
    info = data2[0]['Walking']['routes'][0]['legs'][0]['start_location']['lng'] # start longitude
    info = data2[0]['Walking']['routes'][0]['legs'][0]['end_location']['lat'] # end latitude
    info = data2[0]['Walking']['routes'][0]['legs'][0]['end_location']['lng'] # end longitude

    info = data2[0]['Walking']['routes'][0]['legs'][0]['duration']['text'] # Walking total time taken
    info = data2[0]['Walking']['routes'][0]['legs'][0]['distance']['text'] # Walking total distance travelled

    info = data2[0]['Driving']['routes'][0]['legs'][0]['duration']['text'] # Driving total time taken
    info = data2[0]['Driving']['routes'][0]['legs'][0]['distance']['text'] # Driving total distance travelled
    
    info = data2[0]['Public Transport']['routes'][0]['legs'][0]['duration']['text'] # Transit total time taken
    info = data2[0]['Public Transport']['routes'][0]['legs'][0]['distance']['text'] # Transit total distance travelled

    
# Park St to Pacific Hwy
# Walking Data
    info = data2[1]['Pick Up'] #given pick up location
    info = data2[1]['Drop Off'] #given drop off location
    info = data2[1]['Time'] #given 24hr time
    info = data2[1]['Walking']['routes'][0]['legs'][0]['distance']['text'] #total distance travelled
    info = data2[1]['Walking']['routes'][0]['legs'][0]['start_location']['lat'] #start latitude
    info = data2[1]['Walking']['routes'][0]['legs'][0]['start_location']['lng'] #start longitude
    info = data2[1]['Walking']['routes'][0]['legs'][0]['end_location']['lat'] #end latitude
    info = data2[1]['Walking']['routes'][0]['legs'][0]['end_location']['lng'] #end longitude

    info = data2[1]['Walking']['routes'][0]['legs'][0]['duration']['text'] # Walking total time taken
    info = data2[1]['Driving']['routes'][0]['legs'][0]['duration']['text'] # Driving total time taken
    # info = data2[1]['Public Transport']['routes'][0]['legs'][0]['duration']['text'] # Transit total time taken