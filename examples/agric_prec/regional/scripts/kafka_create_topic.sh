docker-compose exec broker \
    kafka-topics --create --topic test-topic --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
