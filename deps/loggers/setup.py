from setuptools import setup, find_packages

__VERSION__ = '0.12'

setup(name='logger_crud',
      version=__VERSION__,
      description='Logger implementation featuring rotation and console loggers [INTERNAL]',
      url='https://github.com/Tiemma/grpc-crud',
      author='Bakare Emmanuel',
      author_email='emmanueltimmy98@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'logger': ['*.ini']},
      include_package_data=True,
      zip_safe=False)
