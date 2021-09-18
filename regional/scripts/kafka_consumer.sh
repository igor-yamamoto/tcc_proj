docker-compose exec broker \
    kafka-console-consumer --bootstrap-server broker:29092 --topic test-topic --from-beginning \
    #--max-messages 100