docker-compose exec broker \
    kafka-console-consumer --bootstrap-server localhost:29091 --topic test-topic