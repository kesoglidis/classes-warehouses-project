import os
import random
import time
import json
from datetime import datetime, timezone

# import confluent_kafka
from confluent_kafka import Producer

from data_model import get_data

if __name__ == "__main__":
    # Get kafka connection string
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    # Get kafka topic
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "caiso_fuel_mix")
    # Conf for kafka connection
    conf = {'bootstrap.servers': KAFKA_BROKER,'client.id': 'myproducer'}
    # Create the producer
    
    producer = Producer(conf)
    check = True
    while check:
        data = get_data()
        # print(data)
        if data != None:
            print('Valid Response')
            old = data[0]['interval_start_utc']
            check = False
        time.sleep(5)
    old = "2024-12-21T00:00:00+00:00"
    while True:
        start = datetime.now()
        data = get_data()
        if data != None:
            i = -1
            while data[i]['interval_start_utc'] != old:
                print(i)
                data[i]['interval_start_utc']
                msg = data[i]    
                # print(msg)
                msg = json.dumps(msg, indent=2, default=str)

                print(f'Publishing: {msg}')
                producer.produce(KAFKA_TOPIC, msg)
                i -= 1
            old = data[-1]['interval_start_utc']
        time.sleep(10)
