
from os import getenv


class KafkaConfig:

    def __init__(self):
        self.bootstrap_servers = getenv('KAFKA_BROKERS', 'localhost')
        self.client_id = getenv('KAFKA_BROKER_NAME', 'client-0')
        # self.broker_address_family = getenv('KAFKA_BROKER_ADDRESS_FAMILY', 'v4')
        # self.api_version_request = getenv('KAFKA_API_VERSION', 'False')
        # self.broker_version_fallback = getenv('KAFKA_BROKER_VERSION_FALLBACK', '0.8.2.1')
        # self.api_version = (0, 10, 4)

        '''
        Testing out zstd cause of content from this blog
        @see https://blog.cloudflare.com/squeezing-the-firehose/
        
        NOTE: zstd isn't in the confluent library so defaulting to gzip
        Leaving the blog post for reference
        REMEMBER TO BENCHMARK with Grafana
        '''
        self.compression_type = getenv('KAFKA_COMPRESSION_TYPE', 'gzip')
        self.compression_level = getenv('KAFKA_COMPRESSION_LEVEL', '6')


class KafkaProducerConfig(KafkaConfig):

    def __init__(self):
        super(KafkaProducerConfig, self).__init__()

        self.acks = getenv('KAFKA_ACKS', 1)  # Enforce acknowledgement of all messages published
        self.retries = getenv('KAFKA_RETRIES_CONFIG', 2)


class KafkaConsumerConfig(KafkaConfig):

    def __init__(self):
        super(KafkaConsumerConfig, self).__init__()
        self.group_id = getenv('KAFKA_CONSUMER_GROUP_ID', 'consumer-0')
        self.auto_offset_reset = getenv("KAFKA_OFFSET_RESET", 'earliest')
        self.enable_auto_commit = getenv('KAFKA_AUTO_COMMIT_ENABLED', 'true')


def get_config(kafka_config):
    config = dict()
    for key in kafka_config.__dict__:
        config[key.replace('_', '.')] = kafka_config.__dict__[key]
    return config


if __name__ == "__main__":
    print(get_config(KafkaProducerConfig()))
    print(get_config(KafkaConsumerConfig()))
