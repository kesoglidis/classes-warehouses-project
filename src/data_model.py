import json
import requests
import time
from datetime import datetime, timezone


# Function to get live stock data for a symbol
def get_data():
    response = requests.get(f"https://api.gridstatus.io/v1/datasets/caiso_fuel_mix?api_key=2bf76a052c0649929fb96aad00a08fb3&limit=1000")
    time.sleep(1)
    end = str(response.json()['latest_available_time'])
    
    url = f"https://api.gridstatus.io/v1/datasets/caiso_fuel_mix/query?start_time=2024-12-21T00:00Z&end_time=" + end + "&api_key=d561020ab3e44c32a3e605a2a777593d&limit=10000"
    
    response = requests.get(url)
    # print((response.json()['data'])[0].keys())

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        return None
    

def main():
    data = get_data()
    # print(data[-1])


if __name__ == "__main__":
    main()
    
    
