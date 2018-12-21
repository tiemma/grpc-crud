# ES-Kafka-Mongo
Fully automated docker-compose setup for elasticsearch, zookeeper, kafka and mongoDB

- [Elasticsearch](http://elastic.co/)
- [Kafka](https://www.confluent.io/what-is-apache-kafka/)
- [MongoDB](https://www.mongodb.com/)
- [Zookeeper](https://zookeeper.apache.org/)

This docker-compose setup comes packed with the following configs:

#*All kafka services are from the confluent kafka stack*

 - Kafka Connect
 - Kafka Control Center
 - Elasticsearch 2.0
 - MongoDB
 - Zookeeper
 - Schema Registry
 - Kafka Rest
 
There are different service dependencies for each service 

You can run the docker-compose service by doing

> docker-compose up

Or run a specific service 

> docker-compose \<service-name\>

View all available services using

> docker-compose config --services


## Kafka 
Kafka services are configured to run in orders of their dependencies from zookeeper to the final kafka connect configuration.

The config for creating the initial topics used in the Kafka config can be found at this line:


> KAFKA_CREATE_TOPICS: "quickstart-status:1:1,quickstart-offsets:1:1,quickstart-config:1:1"


The initial topics there are needed to be used in the kafka-connect setup and have to be present if such service is running.

Other topics can be added in similar format

> Format:  \<topic-name\>:\<partition-no\>:\<replication-factor-no\>:\<cleanup-policy\>

Cleanup policy can either be compact or delete(DEFAULT).

[Cleanup policy docs](https://archive.cloudera.com/kafka/kafka/2/kafka-0.9.0-kafka2.0.1/configuration.html)

The kafka topics above have been added to satisfy a standalone and distributed config.


## Mongo
You can change the database name to restore your dump to if needed.
I needed to abstract the instances database from my personal computers hence the work in trying to restore.

You could otherwise mount your db location in the /data/db folder using a volume.

The file performing the restore is the entrypoint.sh script.

## Elasticsearch
This starts the server with a default configuration along with an optional docker file config to install plugins.
Mine has a default cloud-aws plugin install for S3 snapshot/restore support.

That can be edited to suit your needs.

You'd need to increase the vm max map counts configuration if you're running on a linux environment

```bash 
 sudo  sysctl -w vm.max_map_count=262144
```



