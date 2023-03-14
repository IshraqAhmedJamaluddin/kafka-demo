from confluent_kafka import Producer

topic = 'ishraq'
client_id = 'ishraq'

conf = {'bootstrap.servers': "34.70.120.136:9094,35.202.98.23:9094,34.133.105.230:9094",
        'client.id': client_id}

producer = Producer(conf)
producer.produce(topic, key="key", value="hola4")
producer.flush()