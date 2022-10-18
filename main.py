import matplotlib.dates
import pandas as pd
import tkinter
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from get_data import Get_data as gd

location = input("Where do you want to travel?")

file = gd(location)

file.get_and_write()

df = pd.read_json("last_year_data.txt")

temp = []

for date in df["location"]["values"]:
    temp.append({"time": date["datetime"],
                 "temp": date["temp"]})

x = [x["time"] for x in temp]
y = [y["temp"] for y in temp]

plt.plot(x, y)
plt.title("Posts: Temperature last year")
plt.xlabel("time")
plt.ylabel("Temp")


plt.show()

