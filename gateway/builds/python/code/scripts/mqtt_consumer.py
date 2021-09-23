import connectors as cns

def pipeline(message):
    return message[0:1]

def run():
    mqtt = cns.mqtt()
    kafka = cns.kafka()

    mqtt.listen(kafka, pipeline)


if __name__ == '__main__':
    run()