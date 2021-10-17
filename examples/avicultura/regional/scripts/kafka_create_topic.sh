docker-compose exec broker-a \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-temperature  --if-not-exists && \
docker-compose exec broker-a \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-humidity  --if-not-exists && \
docker-compose exec broker-a \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-luminosity  --if-not-exists && \
docker-compose exec broker-a \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-ammonia  --if-not-exists
