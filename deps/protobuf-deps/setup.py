from setuptools import setup, find_packages

setup(name='protobuf_deps',
      version='0.12',
      description='Base protobuf classes [INTERNAL]',
      url='https://github.com/Tiemma/grpc-crud',
      author='Bakare Emmanuel',
      author_email='emmanueltimmy98@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'grpcio',
      ],
      package_data={'proto': ['cert/*']},
      include_package_data=True,
      zip_safe=False)
