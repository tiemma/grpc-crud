
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
        self.logger.debug(config)
        self.producer = Producer(config)

    def produce(self, topic, data):

        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                self.logger.debug('Message delivery failed: {}'.format(err))
            else:
                self.logger.debug('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

        try:
            self.producer.poll(0)

            self.producer.produce(topic=topic,
                                  value=data.encode('utf-8'),
                                  callback=delivery_report)

            self.producer.flush()

        except KafkaError as e:
            self.logger.error(
                "Error occurred while sending data %r to topic %r due to error %r",
                data, topic, e)


if __name__ == "__main__":
    print(KafkaProducer().produce("users", "Hello b"))
