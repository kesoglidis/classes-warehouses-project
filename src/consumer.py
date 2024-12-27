import os
import sys
import time

from confluent_kafka import Producer, Consumer, KafkaError, KafkaException

if __name__ == "__main__":
    # Get kafka connection string
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    # Get kafka topic
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "caiso_fuel_mix")
    # Conf for kafka connection
    conf = {'bootstrap.servers': KAFKA_BROKER,'group.id': 'myconsumer'}
    # Create the producer
    consumer = Consumer(conf)
    topics = [KAFKA_TOPIC]
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f'Subscribed to topic <{msg.topic()}> and consumed msg: <{msg.value()}>')
    finally:
        consumer.close()