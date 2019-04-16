# Dev Server setup for the pypi configuration


## PypiRC

This sets the configuration for the pypi server.


## Pip configuration

This contains the api configuration for accessing the pypi server.


## Deployment

Configuration can be built using a docker image, default port is 8080 for the image

```bash
docker build -t pypi:dev .
```

## Run

To run it, we'd just run the image instance on port 8080


```bash 
docker run --name pypi -p 8080:8080 -it pypi:dev

```


## Install from repository

You can use the command below to test that

```bash
pip install --extra-index-url http://localhost:8080/ <PACKAGE>
```


## Install into repsotory

You can use the command likewise

```bash
# Environment configuration if authentication is enabled, enabled by default currently
export TWINE_USERNAME=pypi
export TWINE_PASSWORD=password
twine upload --repository-url http://localhost:8080 dist/* 
```
