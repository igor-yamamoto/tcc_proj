docker-compose exec broker-A \
    kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 3 --partitions 1 --topic devices-temperature  --if-not-exists 

# docker-compose exec broker-A \
#     kafka-topics --create --topic devices-humidity --partitions 1 --replication-factor 2 --if-not-exists --zookeeper zookeeper:2181

# docker-compose exec broker-A \
#     kafka-topics --create --topic devices-luminosity --partitions 1 --replication-factor 2 --if-not-exists --zookeeper zookeeper:2181

# docker-compose exec broker-A \
#     kafka-topics --create --topic devices-ph --partitions 1 --replication-factor 2 --if-not-exists --zookeeper zookeeper:2181

# docker-compose exec broker-A \
#     kafka-topics --list --zookeeper zookeeper:2181
# docker-compose exec zookeeper \
#     kafka --create --topic test-topic --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
