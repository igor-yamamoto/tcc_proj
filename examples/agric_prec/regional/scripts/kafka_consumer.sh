# docker-compose exec broker-A \
#     kafka-console-consumer --bootstrap-server localhost:9091 --topic devices-luminosity

# docker-compose exec broker-B \
#     kafka-console-consumer --bootstrap-server localhost:9092 --topic devices-luminosity

docker-compose exec broker-C \
    kafka-console-consumer --bootstrap-server localhost:9093 --topic devices-luminosity