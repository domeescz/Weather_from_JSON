import json

f = open('names.csv')
data = json.load(f)
#print(data)
weather = (data[0].get("weather"))
#print(weather)
location = data[0].get("formatted_address")
#print(location)
temperature_min = weather.get("temperature")["min"]
temperature_now = weather.get("temperature")["current"]
temperature_max = weather.get("temperature")["max"]
raining = weather.get("rain")["raining"]
intensity = weather.get("rain")["intensity"]
wind = weather.get("wind")["direction"]
wind_speed = weather.get("wind")["speed"]
#print(wind_speed)
#print(wind)
#print(raining)
#print(intensity)
#print(temperature_min)
print(f"""Predikce počasí pro dnešní den:
Lokace: {location},
minimální teplota: {temperature_min} | současná teplota: {temperature_now} | maximální teplota: {temperature_max}""")
if raining:
    if intensity == 'low':
        print("/"*1)
    elif intensity == 'light':
        print("/"*2)
    elif intensity == 'strong':
        print("/"*3)
print(f"""Směr větru: {wind}
Rychlost větru: {wind_speed} km/h
""")
