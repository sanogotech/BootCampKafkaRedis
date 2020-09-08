# TP 1: BootCampKafkaRedis

## Use cases for a streaming platform
Here are some generic scenarios for how you can leverage a streaming platform with the characteristics discussed above:

- **Event-driven processing of big data sets** (e.g., logs, IoT sensors, social feeds)
- Mission-critical, real-time applications (e.g., payments, fraud detection, customer experience)
- **Decoupled integration between different legacy** applications and modern applicationS
- **Microservices architecture**
- Analytics (e.g., for data science, machine learning)
- Website activity tracking

(page views, searches, or other actions users may take) is published to central topics and becomes available for real-time processing, dashboards and offline analytics in data warehouses like Google’s BigQuery.

- **Metrics** :

Kafka is often used for operation monitoring data pipelines and enables alerting and reporting on operational metrics. It aggregates statistics from distributed applications and produces centralized feeds of operational data.

- Log aggregation :

Kafka can be used across an organization to collect logs from multiple services and make them available in standard format to multiple consumers. It provides lower-latency processing and easier support for multiple data sources and distributed data consumption.

- **Stream processing** :

A framework such as Spark Streaming reads data from a topic, processes it and writes processed data to a new topic where it becomes available for users and applications. Kafka’s strong durability is also very useful in the context of stream processing.

- https://axual.com/apache-kafka-use-cases-in-real-life/
- https://blog.ippon.fr/2019/11/18/confluent-schema-registry-un-premier-pas-vers-la-gouvernance-des-donnees/


## Tuning
* log.retention.hours=24
* log.retention.bytes=1073741824

- https://cube.dev/blog/open-source-etl/  : Apache NiFi vs Streamsets
- https://www.cartelis.com/blog/comparatif-logiciels-etl/ : 
- https://arrow.apache.org/
- https://blog.ippon.fr/2020/02/17/apache-knox-api-gateway-hadoop/
- https://blog.ippon.fr/2019/11/04/introduction-a-lelt-et-a-la-solution-matillion/
- Cache : https://www.baeldung.com/apache-ignite-spring-data
- https://blog.ippon.fr/sitemap-posts.xml
- https://blog.ippon.fr/2020/06/26/kafka-dans-un-environnement-multi-datacenter/
- https://blog.ippon.fr/2019/09/16/spark-explique-aux-decideurs/
- https://12factor.net/
- https://blog.ippon.fr/2020/06/15/sonarqube-kill-the-bug-before-its-too-late/


## Kafka  for Windows PATH
* kafka_2.12-2.5.0\bin\windows\*.bat

log.cleanup.policy // delete ou compact  (garde le dernier)
http://kafka.apache.org/documentation/
log.cleanup.policy
The default cleanup policy for segments beyond the retention window. A comma separated list of valid policies. Valid policies are: "delete" and "compact"

Type:	list
Default:	delete
Valid Values:	[compact, delete]
Importance:	medium
Update Mode:	cluster-wide

* cousumer  group-ip // le commit offset d'un membre du groupe impact les autres membres dans la lecture !

![Architecture API Spring Boot Kafka](https://github.com/sanogotech/BootCampKafkaRedis/blob/master/doc/images/DemoSpringBootAPIProducerKafkaConsumerSpringDB.jpg)

## Starting Zookeeper 
nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties &

NB: HD:  3 Machines 3 Zookeeper  et 3 Kafka / 1 par Machine

## Starting Brokers

cp config/server.properties config/server1.properties 

cp config/server.properties config/server2.properties 

cp config/server.properties config/server2.properties 

** server1.properties 
broker.id=1 
listeners=PLAINTEXT://127.0.0.1:9093 
log.dirs=/tmp/kafka-logs1 

- ./bin/kafka-server-start.sh config/server1.properties &
-  ./bin/kafka-server-start.sh config/server2.properties &
-  ./bin/kafka-server-start.sh config/server3.properties &

##  To open the brokers port in the centos firewall

firewall-cmd --zone=public --add-port=9093/tcp –permanent 
firewall-cmd --zone=public --add-port=9094/tcp --permanent 
firewall-cmd --zone=public --add-port=9095/tcp --permanent 
firewall-cmd --reload 

## Creating a Topic
./bin/kafka-topics.sh --create --topic bootcamp-topic --zookeeper localhost:2181 --partitions 3 --replication-factor 2 

It will create a Kafka topic named ‘bootcamp-topic’. The –partition argument describes how many brokers we will use. Since we set up 3 brokers, we can set this option to 3.

## Testing, Connecting and Monitoring our Kafka using Kafka Tools 
Now our Kafka is ready to use, we can monitor Kafka traffic using Kafka Tools that can downloaded from http://www.kafkatool.com/download.html 

![Client GUI KafkaTool](https://github.com/sanogotech/BootCampKafkaRedis/blob/master/doc/images/Kafkatool.jpg)

Tools Open Source:  kafaka-manager  : https://github.com/yahoo/CMAK

## Creating a Producer 


```json
{ 
  "id": 1,
  
   "userId":"souleybas",
 
    "email":"mysouley@oracle.com",
	
    "fullName":"Souleymane SANOGO",

  "password":"basci255"
 }
 ```

## Run
- gradle build    
- java -jar  /targert/*jar

- gradlew bootRun

##  Stop  Kafka
you just need to stop Kafka and Zookeepter properly.

You just have run these two commands in order
```
bin/kafka-server-stop.sh

bin/zookeeper-server-stop.sh
```

# TP 2/ Add Python  Hello Topic /Producer /Consumer

```
pip install kafka-python
```

### Creating Kafka Topics  /myhellotopic

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic myhellotopic

### Python Kafka Consumer  /myhellotopic

https://kafka-python.readthedocs.io/en/master/usage.html

```

from kafka import KafkaConsumer


# To consume latest messages and auto-commit offsets
#consumer = KafkaConsumer('bootcamp-topic',   group_id='my-group',bootstrap_servers=['localhost:9093'])

consumer = KafkaConsumer('bootcamp-topic',bootstrap_servers=['127.0.0.1:9093'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

```

### Kafka Producer  /myhellotopic
```
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
producer.send('bootcamp-topic', b'Akwaba Python').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
#producer = KafkaProducer(retries=5)


print('Send Message to Kafka')
```
### Result 
```
Hello, World! in Kafka using Python
```

# TP3 / Change  Data Capture  with  https://debezium.io/releases/
- https://kafka.apache.org/documentation.html#connect
- https://debezium.io/releases/

~/kafka/bin/connect-standalone.sh ~/sconf/connect-standalone.properties ~/conf/kafka-postgres.properties

* connector-standalone.properties
```
offset.storage.file.filename=/tmp/connect.offsets

plugin.path=/home/ubuntu/software/connect-plugins
```
Add one more property to indicate where the Debezium Postgres connector can be located. Note that this folder should contain all the extracted files form Debezium zip file.


* connector-postgres.properties
```
name=postgres-connector
connector.class=io.debezium.connector.postgresql.PostgresConnector
database.hostname=xxx.xxx.xxx.xxx
database.port=5432
database.user=my_db_user
database.password=my_db_password
database.dbname=my_db_name
database.server.name=db_logical_name
plugin.name=pgoutput
table.whitelist=my_schema.table_name
errors.log.enable=true
errors.logs.include.messages=true
```
* Some of the notable properties are

connector.class – Defines which connector to be used.
plugin.name – In With PostgreSQL 9.5 onwards you can leverage pgoutput instead of decoderbuf. If you are using older version of PostgreSQL, please refer to the Debezium documentation.
table.whitelist – Defines the list of tables (comma separated) which should be observed for data changes.

# TP 4  :  Producer  : ACK /0/1/ALL

```
//import util.properties packages
import java.util.Properties;
//import simple producer packages
import org.apache.kafka.clients.producer.Producer;
//import KafkaProducer packages
import org.apache.kafka.clients.producer.KafkaProducer;
//import ProducerRecord packages
import org.apache.kafka.clients.producer.ProducerRecord;
//Create java class named “SimpleProducer”
public class SimpleProducer {
  public static void main(String[] args) throws Exception{
     // Check arguments length value
     if(args.length == 0){
        System.out.println("Enter topic name”);
        return;
     }
     //Assign topicName to string variable
     String topicName = args[0].toString();
     // create instance for properties to access producer configs
     Properties props = new Properties();
     //Assign localhost id
     props.put("bootstrap.servers", “localhost:9092");
     //Set acknowledgements for producer requests.
     props.put("acks", “all");
     //If the request fails, the producer can automatically retry,
     props.put("retries", 0);
     //Specify buffer size in config
     props.put("batch.size", 16384);
     //Reduce the no of requests less than 0
     props.put("linger.ms", 1);
     //The buffer.memory controls the total amount of memory available to the producer for buffering.
     props.put("buffer.memory", 33554432);
     props.put("key.serializer",
        "org.apache.kafka.common.serializa-tion.StringSerializer");
     props.put("value.serializer",
        "org.apache.kafka.common.serializa-tion.StringSerializer");
     Producer<String, String> producer = new KafkaProducer
        <String, String>(props);
     for(int i = 0; i < 10; i++)
        producer.send(new ProducerRecord<String, String>(topicName,
           Integer.toString(i), Integer.toString(i)));
              System.out.println(“Message sent successfully”);
              producer.close();
  }
}


```
Execution
Further, using the following command, we can execute the application.

java -cp “/path/to/kafka/kafka_2.11-0.9.0.0/lib/*”:. SimpleProducer <topic-name>

## Admin Operations
https://data-flair.training/blogs/kafka-operations/
