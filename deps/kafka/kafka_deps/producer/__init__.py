
from pickle import dumps

from confluent_kafka import Producer, KafkaError
from logger import Logger

from kafka_deps.config import KafkaProducerConfig, get_config


class KafkaProducer:
    """
    Kafka Producer class implementing functions for publishing data to topics
    """

    logger = Logger.get_logger(__name__)

    def __init__(self):
        self.config = get_config(KafkaProducerConfig())
        self.logger.debug('Configuration for producer instance: %r', self.config)
        self.producer = Producer(self.config)

    def produce(self, topic, data, key=None):
        """

        :param topic:
        :param data:
        :param key:
        """
        def delivery_report(err, msg):
            """
            Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush().

                :param err:
                :param msg:
            """
            if err is not None:
                self.logger.debug('Message delivery failed: %r', err)
            else:
                self.logger.debug('Message delivered to %s on partition [%s] with key %s', msg.topic(), msg.partition(), msg.key())

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
        self.logger.info("Producer with client ID %s is shutting down", self.config['client.id'])


if __name__ == "__main__":
    print(KafkaProducer().produce("users", KafkaProducerConfig()))
