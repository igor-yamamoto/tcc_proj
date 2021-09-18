from paho.mqtt import client as mqtt_client
from kafka import KafkaProducer
import decouple
import random

# print(decouple.config('MQTT_TOPIC'))

broker = 'localhost'
topic = 'devices/device1'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'

producer = KafkaProducer(
    bootstrap_servers=['broker:29092'],
    # value_serializer=lambda x: dumps(x).encode(‘utf-8’)
)

def produce_kafka(message):
    producer.send('test-topic', value=b'aaaaa')
    producer.flush()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        message = msg.payload.decode()
        print(f"Received `{message}` from `{msg.topic}` topic")

        print("sending message to kafka")
        print(f"encoded message: {(message.encode('utf-8'))}")
        print(f"byte-encoded message: {bytes(message.encode('utf-8'))}")
        produce_kafka(message.encode('utf-8'))

    client.subscribe(topic)
    client.on_message = on_message

def run():
    # client = connect_mqtt()
    # subscribe(client)
    # client.loop_forever()
    produce_kafka('teste')

if __name__ == '__main__':
    run()

    # client = connect_mqtt()
    # subscribe(client)