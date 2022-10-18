import requests
import json


class Get_data:

    def __init__(self, location):
        self.visualcrossing_api = "4TW9J99JPRJRYEX9AB8BR644W"
        self.location = location

        self.parameters = {
            "aggregateHours": 24,
            "period": "lastyear",
            "contentType": "json",
            "unitGroup": "metric",
            "locationMode": "single",
            "key": self.visualcrossing_api,
            "locations": self.location,
        }

    def get_data(self):
        response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/"
                                    "services/weatherdata/history", params=self.parameters)
        response.raise_for_status()
        data = response.json()
        return data

    def write_data(self, data):
        with open('last_year_data.txt', 'w') as file:
            file.write(json.dumps(data))

    def get_and_write(self):
        data1 = self.get_data()
        self.write_data(data1)

