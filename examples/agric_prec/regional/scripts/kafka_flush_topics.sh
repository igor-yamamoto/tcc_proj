# docker-compose exec broker-A \
#     kafka-topics --zookeeper zookeeper:2181 --delete --topic \
#     # devices-humidity,\
#     devices-luminosity,\
#     devices-ph,\
#     devices-temperature,\
#     devices_humidity,\
#     devices_luminosity,\
#     devices_temperature,\
#     test-topic 
    

#!/bin/bash

TOPICS=$(docker-compose exec broker-A kafka-topics --zookeeper zookeeper:2181 --list )

for T in $TOPICS
do
  if [ "$T" != "__consumer_offsets" ]; then
    docker-compose exec broker-A kafka-topics --zookeeper zookeeper:2181 --delete --topic $T
  fi
done