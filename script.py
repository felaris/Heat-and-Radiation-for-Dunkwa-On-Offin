# Importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the .csv Dataset
clear_sky_data = pd.read_csv(
    'clear_sky_radiation_for-DunkwaOnOffin_2021-04-16.csv')
net_solar_data = pd.read_csv(
    'net_solar_heatnet-solar-heat-for-DunkwaOnOffin_2021-04-16.csv')

# Declaring the time into a Dataframe
hour = pd.DataFrame({
    'hour': ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
})


# Coverting the read data into a Dataframe
clear_sky = pd.DataFrame(clear_sky_data)

net_solar = pd.DataFrame(net_solar_data)


# Placing Both Clear_Sky and Net_Solar into Columns
x = clear_sky.rename(columns={'#   value ': 'clear-sky-radiation'})

y = net_solar.rename(columns={'#   value ': 'net-solar-radiation'})


# Joining all of them into a perfect table
frames = [hour, x, y]
main_data = pd.concat(frames, axis=1)

# Declaring colors for the plot
colours = ['green', '#D31414']
# marker_color = ['#00FF00', '#0F00F0']

# Ploting the graph
main_data.plot(x='hour', y=['clear-sky-radiation', 'net-solar-radiation'], color=colours, marker="o",  markerfacecoloralt='black', markersize=8, linewidth=3, figsize=(14, 10),
               grid=True, title='Plot of Clear Sky radiation and Net Solar radiation against 24hours time interval  for Dunkwa-On-Offin on  16-04-2021 ')


# Grid control
plt.grid(color='#000000', linestyle='-', linewidth=0.9)


# Legend Control
plt.legend(loc='upper left', labels=[
           'clear-sky-radiation', 'net-solar-radiation'])

# Saving the graph as a picture
plt.savefig('Radiation_Analysis_graph.png')
plt.show()
