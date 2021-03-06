from kafka import KafkaConsumer


# To consume latest messages and auto-commit offsets
#consumer = KafkaConsumer('my-topic',   group_id='my-group',bootstrap_servers=['127.0.0.1:9093'])

# consume earliest available messages, don't commit offsets
consumer = KafkaConsumer('my-topic',bootstrap_servers=['127.0.0.1:9093'],auto_offset_reset='earliest',enable_auto_commit=False)




for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


    


