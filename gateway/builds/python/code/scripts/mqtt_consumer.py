from paho.mqtt import client as mqtt_client
from kafka import KafkaProducer
from decouple import config
import random

# print(decouple.)

broker = config('MQTT_URL')
topic = config('MQTT_TOPIC')
port = int(config('MQTT_PORT'))
client_id = f'python-mqtt-{random.randint(0, 1000)}'

KAFKA_URL = config('KAFKA_URL')
KAFKA_PORT = config('KAFKA_PORT')
KAFKA_BROKER = f'{KAFKA_URL}:{KAFKA_PORT}'
KAFKA_TOPIC = config('KAFKA_TOPIC')

print(KAFKA_BROKER)

producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER],
    # value_serializer=lambda x: dumps(x).encode(‘utf-8’)
)

def produce_kafka(message):
    producer.send(KAFKA_TOPIC, value=bytes(message))
    # producer.flush()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        message = msg.payload.decode()
        print(f"Received `{message}` from `{msg.topic}` topic")

        print("sending message to kafka")
        produce_kafka(message.encode('utf-8'))

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    # produce_kafka('teste')

if __name__ == '__main__':
    run()

    # client = connect_mqtt()
    # subscribe(client)