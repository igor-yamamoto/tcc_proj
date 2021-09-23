import connectors as cns
import pipeline as pl

def pipeline(message):
    return message[0:1]

def run():
    mqtt = cns.mqtt()
    kafka = cns.kafka()
    pipeline = pl.main

    mqtt.listen(kafka, pipeline)


if __name__ == '__main__':
    run()