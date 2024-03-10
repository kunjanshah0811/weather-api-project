import requests


class City:
    def __init__(self,name, lat, lon, units="metric"):
        self.name=name
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()
        self.temp_print()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=79007029562c2ab46617d801d8018750")


        except:
            print("No internet access 😊")


        self.response_json=response.json()
        self.temp=self.response_json['main']['temp']
        self.temp_min=self.response_json['main']['temp_min']
        self.temp_max=self.response_json['main']['temp_max'] 

    def temp_print(self):

        
        print(f"\nIn {self.name} it it currently {self.temp} ℃")
        print(f"Today's High: {self.temp_max} ℃")
        print(f"Today's Low: {self.temp_min} ℃ \n")



my_city=City("Paderborn",51.7189,8.7575)
vacation_city=City('Vadodara', 22.310696,73.192635)
#print(vacation_city.response_json)
        