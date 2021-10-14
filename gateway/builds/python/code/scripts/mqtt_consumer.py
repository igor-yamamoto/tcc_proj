import connectors as cns
import pipeline as pl

def run():
    mqtt = cns.mqtt()
    kafka = cns.kafka()
    pipeline = pl.main

    mqtt.listen(kafka, pipeline)


if __name__ == '__main__':
    run()