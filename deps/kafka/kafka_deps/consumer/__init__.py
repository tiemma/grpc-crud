

from pickle import loads

from confluent_kafka import Consumer
from logger import Logger

from kafka_deps.config import KafkaConsumerConfig, get_config


class KafkaConsumer:
    """
    Kafka Consumer class defining functions for subscribing to topic data publishing
    """

    logger = Logger.get_logger(__name__)

    def __init__(self):
        self.config = get_config(KafkaConsumerConfig())
        self.logger.debug('Configuration for consumer instance: %r', self.config)
        self.consumer = Consumer(self.config)

    def subscribe(self, topics):
        """

        :param topics:
        """
        self.consumer.subscribe(topics.split(','))

        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                self.logger.error("Consumer error: {}".format(msg.error()))
                continue

            data = loads(msg.value())
            self.logger.debug('Received data from consumer for {topic=%s, key=%s, partition=%s, offset=%s, data=%s}',
                              msg.topic(), msg.key(), msg.partition(), msg.offset(), data)

            yield data

    def __del__(self):
        self.logger.info("Consumer with group ID %s is shutting down", self.config['group.id'])
        self.consumer.close()


if __name__ == "__main__":
    for i in KafkaConsumer().subscribe("users"):
        print(i)
