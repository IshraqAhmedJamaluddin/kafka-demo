import sys
import os
from dotenv import load_dotenv
from confluent_kafka import Consumer, KafkaError, KafkaException

topic = 'ishraq'
group_id = 'ishraq'

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS')

conf = {'bootstrap.servers': BOOTSTRAP_SERVERS,
        'group.id': group_id,
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

try:
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print('message received', msg.value())
finally:
    consumer.close()