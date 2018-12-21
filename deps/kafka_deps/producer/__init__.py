
from pickle import dumps

from confluent_kafka import Producer, KafkaError
from logger import Logger

from os.path import abspath
from sys import path
lib_path = abspath('..')
path.insert(0, lib_path)

from config import KafkaProducerConfig, get_config


class KafkaProducer:

    logger = Logger.get_logger(__name__)

    def __init__(self):
        config = get_config(KafkaProducerConfig())
        self.logger.debug('Configuration for producer instance: %r', config)
        self.producer = Producer(config)

    def produce(self, topic, data, key=None):

        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                self.logger.debug('Message delivery failed: %r', err)
            else:
                self.logger.debug('Message delivered to %s on partition [%s]', msg.topic(), msg.partition())

        try:
            self.producer.poll(0)

            self.producer.produce(topic=topic,
                                  # Dumping data with pickle as we can also publish binary data
                                  value=dumps(data),
                                  key=key,
                                  callback=delivery_report)

            self.producer.flush()

        except KafkaError as e:
            self.logger.error(
                "Error occurred while sending data %r to topic %r due to error %r",
                data, topic, e)

    def __del__(self):
        self.logger.info("Producer with group ID %s is shutting down", self.config['group.id'])


if __name__ == "__main__":
    print(KafkaProducer().produce("users", KafkaProducerConfig()))
