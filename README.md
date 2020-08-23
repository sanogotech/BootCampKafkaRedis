# BootCampKafkaRedis

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

## Creating a Producer 



