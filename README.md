# TP 1: BootCampKafkaRedis

![Architecture API Spring Boot Kafka](https://github.com/sanogotech/BootCampKafkaRedis/blob/master/doc/images/DemoSpringBootAPIProducerKafkaConsumerSpringDB.jpg)

## Starting Zookeeper 
./bin/zookeeper-server-start.sh config/zookeeper.properties &

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

```
from kafka import KafkaConsumer
consumer = KafkaConsumer('myhellotopic')
for message in consumer:
    print (message)
```

### Kafka Producer  /myhellotopic
```
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
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


