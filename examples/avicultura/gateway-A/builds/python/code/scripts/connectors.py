from paho.mqtt import client as mqtt_client
from kafka import KafkaProducer, KafkaConsumer
from decouple import config
import random
import time

class kafka:
    def __init__(self):
        KAFKA_URL = config('KAFKA_URL')
        self.port = config('KAFKA_PORT')
        self.broker = f'{KAFKA_URL}:{self.port}'
        self.topic = config('KAFKA_TOPIC')

        flush = config('KAFKA_FLUSH')
        if flush == 'True':
            self.flush = True
        else:
            self.flush = False

        attempt_retry = config('KAFKA_ATTEMPT_RETRY')
        if attempt_retry == 'True':
            print('Attempt retry configured to true. Extracting attempts parameters.')

            self.attempt_retry = True
            self.wait_time = int(config('KAFKA_WAIT_TIME'))
            self.max_retires = int(config('KAFKA_MAX_RETRIES'))
            self.retry_count = 0
        else:
            self.attempt_retry = False

        try:
            self.connect()
            self.connect_status = 0
        except:
            print(f'Cannot stablish connection to topic {self.topic} at {self.broker}.')
            self.connect_status = 400

    def connect(self):
        connection_test = self.consume()
        if connection_test:
            print(f"Connected to KAFKA Broker! \n\tbroker: {self.broker} \n\ttopic: {self.topic}")
            print("Establishing producer connection to broker")

            self.producer = KafkaProducer(
                bootstrap_servers=[self.broker]
            )
        else:
            if self.attempt_retry:
                while self.retry_count <= self.max_retries:
                    print(
                        f"Failed to connect. Attempting retry n{self.retry_count+1}")
                    time.sleep(self.wait_time)

                    self.retry_count += 1

                    self.connect()
                else:
                    print("Failed to connect.")
            else:
                print("Failed to connect.")

    def consume(self):
        topics = KafkaConsumer(
            bootstrap_servers=[self.broker],
        ).topics()

        if topics:
            test_val = True
        else:
            test_val = False

        return test_val

    def produce(self, message, topic):
        if self.connect_status == 0:
            self.producer.send(topic, value=bytes(message))
        else:
            print('error: connection not stablished with broker.')
        
        if self.flush:
            self.producer.flush()


class mqtt:
    def __init__(self):
        self.broker = config('MQTT_URL')
        self.topic = config('MQTT_TOPIC')
        self.port = int(config('MQTT_PORT'))
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'

        self.user = config('MQTT_USER')
        self.passwd = config('MQTT_PASS')

        debug_mode = config('MQTT_DEBUG')
        if debug_mode == 'True':
            self.debug_mode = True
        else:
            self.debug_mode = False
        print(self.debug_mode)

        attempt_retry = config('MQTT_ATTEMPT_RETRY')
        if attempt_retry == 'True':
            print('Attempt retry configured to true. Extracting attempts parameters.')

            self.attempt_retry = True
            self.wait_time = int(config('MQTT_WAIT_TIME'))
            self.max_retires = int(config('MQTT_MAX_RETRIES'))
            self.retry_count = 0
        else:
            self.attempt_retry = False

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            type(rc)
            if rc == 0:
                print(f"Connected to MQTT Broker! \n\tbroker: {self.broker}:{self.port} \n\ttopic: {self.topic}")
            else:
                if self.attempt_retry:
                    while self.retry_count <= self.max_retries:
                        print(
                            f"Failed to connect. Attempting retry n{self.retry_count+1}")
                        time.sleep(self.wait_time)

                        self.retry_count += 1

                        self.connect()
                    else:
                        print("Failed to connect, return code %d\n", rc)
                else:
                    print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        print(self.broker, self.port)
        client.username_pw_set(self.user, self.passwd)
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client, broker, pipeline):
        def on_message(client, userdata, msg):
            message = msg.payload.decode()

            if self.debug_mode:
                print(f"Received `{message}` from `{msg.topic}` topic")

            if callable(pipeline):
                message_transf = pipeline(message)
                
            if message_transf:
                message = message_transf[0]
                topic_context = message_transf[1]
                print(message, topic_context)
                if len(topic_context) > 1:
                    topic = f'{broker.topic}-{topic_context}'
                else:
                    topic = broker.topic
                print(f"\t Sending message to kafka topic {topic}")
                try:
                    broker.produce(message.encode('utf-8'), topic=topic)
                except:
                    broker.produce(message, context=topic)

        client.subscribe(self.topic)
        client.on_message = on_message

    def listen(self, kafka_broker: kafka, pipeline):
        client = self.connect()
        self.subscribe(client, kafka_broker, pipeline)
        client.loop_forever()