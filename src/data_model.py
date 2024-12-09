import json
import requests
import time
from datetime import datetime, timezone


# Function to get live stock data for a symbol
def get_data():
    response = requests.get(f"https://api.gridstatus.io/v1/datasets/caiso_fuel_mix?api_key=2bf76a052c0649929fb96aad00a08fb3&limit=1000")
    time.sleep(1)
    end = str(response.json()['latest_available_time'])
    # print(end)

    # url = f"https://api.gridstatus.io/v1/datasets/caiso_fuel_mix/query?api_key=d561020ab3e44c32a3e605a2a777593d&limit=1000"
    url = f"https://api.gridstatus.io/v1/datasets/caiso_fuel_mix/query?start_time=2024-12-09T00:00Z&end_time=" + end + "&api_key=d561020ab3e44c32a3e605a2a777593d&limit=1000"
    # url = f"https://api.gridstatus.io/v1/dataset-updates/caiso_fuel_mix?api_key=2bf76a052c0649929fb96aad00a08fb3&limit=1000" #updates
    response = requests.get(url)
    # response = requests.get(f"https://api.gridstatus.io/v1/datasets/caiso_standardized_5_min?api_key=2bf76a052c0649929fb96aad00a08fb3&limit=1000")
    print(response)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        # print(data['data'][0]['id'])
        # for d in data['data']:
        #     print(d['id'])
        # print(" ")
        # print(data.keys())
        # for i in data:
        #     print(i)
        #     print(type(data[i]))
        #     if(type(data[i]) == list):
        #         print(data[i][0].keys())
        #     else:
        #         if(type(data[i]) == dict):
        #             print(data[i].keys())
        #         else:
        #             print(data[i])
        #     print(" ")
        
        return data['data']
    else:
        return None


# data = get_data()
# print(data)
class Dataset:

    def __init__(self, time, temperature):
        self.time = time
        self.temperature = temperature


    def __dict__(self):
        return {
            "time": self.time,
            "temperature": self.temperature
        }

    def __repr__(self):
        res = self.__dict__()
        return json.dumps(res, indent=2, default=str)
    
    
