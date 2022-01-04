# Import Meteostat library and dependencies
from datetime import date, datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Daily

# Set coordinates of Lviv
lat = 49.8383
lon = 24.0232

## Set time period
# start = datetime(2021, 12, 9)
# end = datetime(2021, 12, 18)

## Set second time period
# start_1 = datetime(2020, 12, 9)
# end_1 = datetime(2020, 12, 18)

def dateedit(input_str):
    date_var = input(input_str)
    """change data format"""
    year, month, day = map(int, date_var.split('-'))
    date1 = datetime(year, month, day)
    return date1

## User input for comparison
start = dateedit("Enter start date in YYYY-MM-DD format: ")
end = dateedit("Enter end date in YYYY-MM-DD format: ")

start_1 = dateedit("Enter start date in YYYY-MM-DD format: ")
end_1 = dateedit("Enter end date in YYYY-MM-DD format: ")

# Get closest weather station to Lviv
stations = Stations()
stations = stations.nearby(lat, lon)
stations = stations.inventory('daily', (start, end))
station = stations.fetch(1)


# Get daily data for 2021 at the selected weather station
data = Daily(station, start, end)
data = data.fetch()

# Get daily data for 2020 at the selected weather station
data_1 = Daily(station, start_1, end_1)
data_1 = data_1.fetch()

# Reset our index so datetime_utc becomes a column
data.reset_index(inplace=True)
data_1.reset_index(inplace=True)

# Create new columns
data['month-day'] = data['time'].dt.strftime('%m-%d')
data['year'] = data['time'].dt.year

# Create new columns
data_1['month-day'] = data_1['time'].dt.strftime('%m-%d')
data_1['year'] = data_1['time'].dt.year

# Check the data info
#print(data)
#print(data_1)

# # Plot line chart including minimum and maximum temperature
plt.style.use('seaborn')
#data.plot(y=['tmin', 'tmax'])

ax = data.plot(x='month-day', y=['tmin', 'tmax'], label=['tmin ' + str(start.year), 'tmax ' + str(start.year)])
ax = data_1.plot(x='month-day', y=['tmin', 'tmax'], label=['tmin ' + str(start_1.year), 'tmax ' + str(start_1.year)], ax=ax)

# Format plot.
#plt.title("Daily high and low temperatures - Lviv", fontsize=20)
plt.title("Temperature comparison", fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel("Temperature (°C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
