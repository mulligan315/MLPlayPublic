import requests

response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=b1f7ac36d27c4b11a7913714231705&q=Calgary&days=2&aqi=yes&alerts=no")

current_weather_json=response.json()
current=current_weather_json.get('current')
forecast = current_weather_json.get('forecast').get('forecastday')
forecast_today = forecast[0].get('day')
forecast_tomorrow = forecast[1].get('day')
print(current_weather_json.get('location').get('name'),"\n")
print("Current Temp: ",current.get('temp_c'),"C",sep='')
print("Feels Like: ",current.get('feelslike_c'),"C",sep='')

pm2_5=round(float(current.get('air_quality').get('pm2_5')),1)
co=float(current.get('air_quality').get('co'))
no2=float(current.get('air_quality').get('no2'))
o3=float(current.get('air_quality').get('o3'))
so2=float(current.get('air_quality').get('so2'))
pm10=float(current.get('air_quality').get('pm10'))

pm2_5_lo=[0,12.1,35.5,55.5,150.5,250.5,350.5]
pm2_5_hi=[12,35.4,55.4,150.4,250.4,350.4,500.4]
AQI_lo=[0,51,101,151,201,301,401]
AQI_hi=[50,100,150,200,300,400,500]

pm2_5_index=0

for index in range(0,7):
    if pm2_5 >= pm2_5_lo[index] and pm2_5 < pm2_5_hi[index]:
        pm2_5_index=index
        break
    
pm2_5_AQI=(AQI_hi[pm2_5_index] - AQI_lo[pm2_5_index])/(pm2_5_hi[pm2_5_index] - pm2_5_lo[pm2_5_index])*(pm2_5 - pm2_5_lo[pm2_5_index]) + AQI_lo[pm2_5_index]

print("PM2.5 AQI: ",str(round(pm2_5_AQI)),sep='')
print("\nToday's Forecast:\n")
print("Hi: ",forecast_today.get('maxtemp_c'),"C",sep='')
print("Lo: ",forecast_today.get('mintemp_c'),"C",sep='')
print("Precip: ",forecast_today.get('daily_chance_of_rain'),"%",sep='')
print("\nTomorrow's Forecast:\n")
print("Hi: ",forecast_tomorrow.get('maxtemp_c'),"C",sep='')
print("Lo: ",forecast_tomorrow.get('mintemp_c'),"C",sep='')
print("Precip: ",forecast_tomorrow.get('daily_chance_of_rain'),"%",sep='')