import requests

'''
you can register here 
https://openweathermap.org/api
in order to get an API
'''

API_KEY = "{your api}"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter city please: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code  == 200:
    data = response.json() 
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] -273.15,2)
    print("temperature: ",temperature," degrees celcious \nweather: ",weather) 

else:
    print("request failed")














