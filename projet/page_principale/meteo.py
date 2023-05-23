import requests

class Meteo():
        def __init__(self):
                self.url = 'http://api.openweathermap.org/data/2.5/weather?q=Gardanne,FR&appid=ac7c75b9937a495021393024d0a90c44&units=metric'

                self.res = requests.get(self.url)
                self.data = self.res.json()
                self.temp = self.data['main']['temp']
                self.win_speed = self.data['wind']['speed']
                self.latitude = self.data['coord']['lat']
                self.longitude = self.data['coord']['lon']
                self.description = self.data['weather'][0]['description']

                print(self.res)
                print("-----")
                print("Temperature : {} °C".format(self.temp))
                print("Wind speed : {} m/s".format(self.win_speed))
                print("Latitude : {}".format(self.latitude))
                print("Longitude : {}".format(self.longitude))
                print("Description : {}".format(self.description))
        
        def temperature(self):
                return self.temp        
        
        def description(self):
                return self.description
        


