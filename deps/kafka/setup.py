from setuptools import setup, find_packages

__VERSION__ = '0.12'

setup(name='kafka_deps',
      version=__VERSION__,
      description='Package containing code for publishing and consumin data [INTERNAL]',
      url='https://github.com/Tiemma/grpc-crud',
      author='Bakare Emmanuel',
      author_email='emmanueltimmy98@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'confluent-kafka',
            'logger-crud',
            'protobuf-deps'
      ],
      package_data={'kafka_deps': ['.env']},
      include_package_data=True,
      zip_safe=False)
