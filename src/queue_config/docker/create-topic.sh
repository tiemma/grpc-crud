#!/bin/bash

if [[ -z "$KAFKA_CREATE_TOPICS" ]]; then
    exit 0
fi

#Specify alternative seperator, otherwise use a comma
IFS="${KAFKA_CREATE_TOPICS_SEPARATOR-,}";


#Run through specified topics and create them
for topicToCreate in $KAFKA_CREATE_TOPICS; do

    echo "creating topics: $topicToCreate"
    IFS=':' read -r -a topicConfig <<< "$topicToCreate"

    config=
    if [ -n "${topicConfig[3]}" ]; then
        config="--config=cleanup.policy=${topicConfig[3]}"
    fi
    
    COMMAND="kafka-topics \\
		--create \\
		--zookeeper ${KAFKA_ZOOKEEPER_CONNECT} \\
		--topic ${topicConfig[0]} \\
		--partitions ${topicConfig[1]} \\
		--replication-factor ${topicConfig[2]} \\
		${config} \\
		--if-not-exists "
    echo $COMMAND
    eval "${COMMAND}"
done

wait
