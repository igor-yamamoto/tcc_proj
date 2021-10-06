docker-compose exec broker-A \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-temperature  --if-not-exists && \
docker-compose exec broker-A \
kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-humidity  --if-not-exists && \
docker-compose exec broker-A \
kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-luminosity  --if-not-exists && \
docker-compose exec broker-A \
kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 2 --partitions 10 --topic devices-ph  --if-not-exists

# docker-compose exec broker-A \
#     kafka-topics --list --zookeeper zookeeper:2181
# docker-compose exec zookeeper \
#     kafka --create --topic test-topic --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
