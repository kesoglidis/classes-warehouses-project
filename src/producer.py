import os
import random
import time
from datetime import datetime

from confluent_kafka import Producer

from src.data_model import Dataset

if __name__ == "__main__":
    # Get kafka connection string
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    # Get kafka topic
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "temperature")
    # Conf for kafka connection
    conf = {'bootstrap.servers': KAFKA_BROKER,'client.id': 'myproducer'}
    # Create the producer
    producer = Producer(conf)
    while True:
        # Get a random value
        temp = random.uniform(15.0, 40.0)
        # Create the object
        temperature = Dataset(datetime.now(), temp)
        # Get the msg in json format
        msg = temperature.__repr__()
        # Publish the msg
        print(f'Publishing: {msg}')
        producer.produce(KAFKA_TOPIC, msg)
        # Wait 1 second and publish again
        time.sleep(1)
