
01. Cluster 2 ou 3 Broker ! // Plusieurs Zookeeper !!! par domaine metier
01. Replication factor  creation des partitions
0.log.dirs=kafkalogs3  // log.retention.hours=-1 //log.retention.hours=168 // log.retention.hours=24 // logs = messages !!!!
1. Producer :  Choix de la particition §§§ , key ! Value !
2. Producer Retry
3. Producer Feedback : # Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)


# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')
-------------------------------------------------------------------
4. Consumer : Connect, Coupure et Reconnect Consumer !!! Offset §
5. Notion de groupe consumer !! et notion de consumer offset !!!
6.  Chance Data Capture  via  Kafka Connect + plugin Debezium  Redhat vs Spring Solution  vs  StreamSet pipeline
7.  Apache Nifi vs Apache Kafka Connect  vs StreamSets
8.  Apache KafkaconnectSink 
9.  Apache Stream  vs Spark Stream
10.  Gestions des exceptions
11.  Temps réel // exemple bourse ! // visualisation
12.  Kafka comme base de données !!! vs offset lecture §§§
13.  Avantage Apache Confluent , Docker !!, Apache Connect,
14 . # StopIteration if no message after 1sec //KafkaConsumer(consumer_timeout_ms=1000)
15. consume earliest available messages, don't commit offsets
16.  _consumer_offset !!!
17. # To consume latest messages and auto-commit offsets
18.  Create Topics :  bin/kafka-topics.sh  --zookeeper localhost:2181 --create --topic myNewTopic --partitions 10 --replication-factor 3
19.  Sécurité !!
20. API Admin Apache