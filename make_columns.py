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
    print(data2[0])