import json
import os


with open("problem_train_station_data.json", "r") as ts:
    stations = json.load(ts)
    for s in stations:
        if not s.get("error_message"):
            name = s["results"][0]["address_components"][0]["short_name"]
            lat = s["results"][0]["geometry"]["location"]["lat"]
            lng = s["results"][0]["geometry"]["location"]["lng"]
            print(f"{name}, lat:{lat}, lon:{lng}")
        else:
            print()
