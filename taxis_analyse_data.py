#%%
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import pandas as pd

#%%
path = "in"
df = pd.read_excel(os.path.join(path, "taxis.xlsx"))
df.Date = pd.to_datetime(df.Date, dayfirst=True)
df.index = df["datetime"]
df.sample(3)

#%%
most_expensive = df.loc[df["Total Amount (inc GST)"].idxmax()]
least_expensive = df.loc[df["Total Amount (inc GST)"].idxmin()]
#%%
print(
    f"""If we take all the CabCharge Data for 2019, what can we find out from it?

As of {df.datetime.max().strftime('%A %d of %B')}, Sydney BVN people have taken {df.shape[0]} taxi rides. 

The most expensive trip was on {most_expensive.datetime.strftime('%A %d %B at %I:%M%p')}, it was ${most_expensive['Total Amount (inc GST)']}, it was from {most_expensive['Pick Up']} to {most_expensive['Drop Off']}, and didn't get claimed by a person.

The least expensive trip was on {least_expensive.datetime.strftime('%A %d %B at %I:%M%p')}, it was ${least_expensive['Total Amount (inc GST)']}, it was from {least_expensive['Pick Up']} to {least_expensive['Drop Off']}. The places in CAPS are how the system reports the locations. Some of the cabs report street names, others just give you AIRPORT, CITY or SUBURBS.

I've calculated a CO₂ amount for each trip. This is done like this:

```
HireCharge = 3.60
DistanceRate = 2.19
kgCO2perkm = 0.098
kg = ((row["Fare (inc GST)"] - HireCharge) / DistanceRate) * kgCO2perkm
```

The taxi costs come from [here](https://transportnsw.info/travel-info/ways-to-get-around/taxi-hire-vehicle/rank-hail-taxi-fares-charges) and the taxi is assumed to be a hybrid Camry.

This method doesn't take into account that night time trips are more expensive, and therefore emit slightly less than claimed, but it could be extended to track that. For the moment I'm happy with these numbers.

I'm guessing that what you really care about is the total for the year, so here it is: {round(df.kg_co2.sum(), 1)}kg of CO₂. 
AKA {round(df.kg_co2.sum()/1000, 1)} tonnes of CO₂. That sounds like a big number, so to put it into some context, a business class trip, one way from Sydney to New York is 7.009 tonnes of CO₂.
It _is_ a big number, but it's only one of the big numbers that I'll be talking about in the next few days.

The vast majority of the trips taken are are around the 1kg of CO₂. (The median is {round(df.kg_co2.median(), 3)}Kg of CO₂. There are a very small number of trips over 5kg of CO₂.
"""
)
#%%
df.hist(column="kg_co2", bins=40, grid=False)
plt.title("Histogram of CO₂ emitted per trip")
plt.ylabel("Number of trips")
plt.xlabel("Kg of CO₂ emitted on that trip")

#%%
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.scatter(list(df.date), list(df.time), s=df.kg_co2)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

major_formatter = mdates.DateFormatter("%H:%M")
print(major_formatter)
ax.yaxis.set_major_locator(plt.MaxNLocator(23))  # mdates.HourLocator())
# ax.yaxis.set_major_formatter(major_formatter)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

fig.autofmt_xdate()


#%%
anonDF = df[df.Name == " - "]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.scatter(list(anonDF.date), list(anonDF.time), s=anonDF.kg_co2)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


major_formatter = mdates.DateFormatter("%H:%M")
print(major_formatter)
ax.yaxis.set_major_locator(plt.MaxNLocator(23))  # mdates.HourLocator())
# ax.yaxis.set_major_formatter(major_formatter)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

fig.autofmt_xdate()
print(ax.yaxis.get_major_locator())
print(ax.yaxis.get_minor_locator())

#%%
co2ranking = df.groupby(["Name"]).sum().kg_co2.sort_values(ascending=False)
#%%
print("Who are the top ten taxi users in 2019, based on CO₂?")
co2ranking[:10]
#%%
print("Who generates the least CO₂ by using taxis?")
print("If you don't use taxis at all, you're not on this list.")
co2ranking[-10:]
#%%
print("Each taxi has a code. Which taxi carries BVN people the most?")
most_used_taxis = df.Taxi.value_counts()[:5]
most_used_taxis
#%%
print(
    f"The number one taxi, serving BVN is {most_used_taxis.index[0]}, "
    "but it's not used by anyone particularly much. "
    "If you're on this list, did you notice that "
    "you'd got in twice?"
)
df[df.Taxi == most_used_taxis.index[0]].Name.value_counts()
#%%
print(f"How about the second most used taxi, {most_used_taxis.index[1]}?")
taxi_love = df[df.Taxi == most_used_taxis.index[1]]
taxi_love.Name.value_counts()

#%%
print("Looks like someone has a favourite taxi! Or could it be just an anomaly?")
rider = taxi_love.Name.value_counts().index[0]
df[df.Name == rider].Taxi.value_counts().plot(kind="pie")
plt.title(f"{rider}'s taxis")

#%%
print("who takes the most cabs, by count?")
df.Name.value_counts()[:10]
#%%
print("what about by emissions?")
df.groupby("Name").sum().kg_co2.sort_values(ascending=False)[:10]


#%%
print("Let's look at the early trips")
early = df[[3 <= dt.time().hour <= 6 for dt in df.datetime]]
early.sample(10)

#%%
early["Drop Off"].value_counts()[:25]
#%%
early["Pick Up"].value_counts()[:25]

#%%
early.Name.value_counts()

#%%
df.resample("W").sum().kg_co2.plot()
plt.style.context("seaborn-pastel")
plt.grid(True, axis="x", linestyle="--", linewidth=1)
plt.title("kg of CO₂ emitted by BVN Sydney's taxi use, summed by week")
plt.ylabel("kg of CO₂")
plt.xlabel("Week")


#%%

