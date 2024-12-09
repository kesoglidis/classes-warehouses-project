import os
import random
import time
import json
from datetime import datetime, timezone

# import confluent_kafka
from confluent_kafka import Producer

from data_model import Dataset
from data_model import get_data

if __name__ == "__main__":
    # Get kafka connection string
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    # Get kafka topic
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "temperature")
    # Conf for kafka connection
    conf = {'bootstrap.servers': KAFKA_BROKER,'client.id': 'myproducer'}
    # Create the producer
    
    producer = Producer(conf)
    check = True
    while check:
        data = get_data()
        # print(data)
        if data != None:
            old = data[0]['interval_start_utc']
            check = False
        time.sleep(5)

    old = "2024-12-09T00:00:00+00:00"
    print(old)
    while True:
        start = datetime.now()
        # print(start)
        data = get_data()
        if data != None:
            # print(data[-1])
            # print(data[0])
            i = -1
            # print(data[0]['interval_start_utc'])
            # print(data[-1]['interval_start_utc'])
            # print(old)
            while data[i]['interval_start_utc'] != old:
                i -= 1
                print(i)
                data[i]['interval_start_utc']
                msg = data[i]    
                # print(msg)
                msg = json.dumps(msg, indent=2, default=str)

                print(f'Publishing: {msg}')
                producer.produce(KAFKA_TOPIC, msg)
            old = data[-1]['interval_start_utc']
        # print(datetime.now()-start)
        # Get a random value
        # temp = random.uniform(15.0, 40.0)
        # # Create the object
        # temperature = Dataset(datetime.now(), temp)
        # # Get the msg in json format
        # msg = temperature.__repr__()
        # # Publish the msg
        # print(f'Publishing: {msg}')
        # producer.produce(KAFKA_TOPIC, msg)
        # # Wait 1 second and publish again
        time.sleep(10)
