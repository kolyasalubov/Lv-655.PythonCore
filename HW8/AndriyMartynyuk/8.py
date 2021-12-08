# Task 1 Calculator
from pyowm.utils import timestamps
from pyowm.utils import config
from pyowm import OWM
import calculator as c

# def numbers():
#     question = int(input(
#         "Hello, what function do you whant to use? Please type 1 for sum, 2 - for minus, 3 - for division, 4 - for multiplication: "))
#     a = int(input("Type number one"))
#     b = int(input("Type number two"))
#     if question == 1:
#         print("Your result is: ", c.my_sum(a, b))
#     elif question == 2:
#         print("Your result is: ", c.my_minus(a, b))
#     elif question == 3:
#         print("Your result is: ", c.my_division(a, b))
#     elif question == 4:
#         print("Your result is: ", c.my_mult(a, b))
#     else:
#         print("Please, enter givven choices")

# numbers()

# Task 2


# ---------- FREE API KEY examples ---------------------

city = input("Please, write the city, you want to check: ")
owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

detailed_status = input(
    "If you want to see detailed status type:  1 - Yes, 2 - No")
wind = input("If you want to see information about wind type : 1 - Yes, 2 - No")
humidity = input("If you want to see humidity type: 1 - Yes, 2 - No")
temperature = input("If you want to see temperature type: 1 - Yes, 2 - No")
rain = input("If you want to see information about rain type: 1 - Yes, 2 - No")
heat_index = input("If you want to see heat index type: 1 - Yes, 2 - No")
clouds = input(
    "If you want to see information about clouds type: 1 - Yes, 2 - No")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(city)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

if detailed_status == "1":
    print(f"Datailed status: {w.detailed_status}")
if wind == "1":
    print("wind speed:", w.wind()['speed'], "wind deg:", w.wind()['deg'])
if humidity == "1":
    print(f"Humidity is {w.humidity}")
if temperature == "1":
    print("Temperature: max ", w.temperature('celsius')['temp_max'], "min ", w.temperature(
        'celsius')['temp_min'], "temperature ", w.temperature('celsius')['temp'])
if rain == "1":
    print(f"Rain: {w.rain}")
if heat_index == "1":
    print(f"Heat Index is {w.heat_index}")
if clouds == "1":
    print(f"Clouds: {w.clouds}")
