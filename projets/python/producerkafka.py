from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9093'])


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
#producer.send('my-topic', b'Akwaba PHP').add_callback(on_send_success).add_errback(on_send_error)
# produce keyed messages to enable hashed partitioning
producer.send('topic-2partition', key=b'Souley', value=b'msg1').add_callback(on_send_success).add_errback(on_send_error)
producer.send('topic-2partition', key=b'Youssef', value=b'msg2').add_callback(on_send_success).add_errback(on_send_error)
producer.send('topic-2partition', key=b'koffi', value=b'msg3').add_callback(on_send_success).add_errback(on_send_error)
producer.send('topic-2partition', key=b'koffi', value=b'msg4').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
#producer = KafkaProducer(retries=5)


print('Send Message to Kafka')


# [12:52] Ben Nour Youssef (Invité)
    # hash(key)%nbr_partitions
# ​[12:52] Ben Nour Youssef (Invité)
    # = partition cible du message 
