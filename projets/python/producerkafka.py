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
producer.send('bootcamp-topic', b'Akwaba PHP').add_callback(on_send_success).add_errback(on_send_error)
# produce keyed messages to enable hashed partitioning
producer.send('bootcamp-topic', key=b'Prenom', value=b'Fabien').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
#producer = KafkaProducer(retries=5)


print('Send Message to Kafka')