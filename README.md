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
