# Publishing local packages for internal use

Since we're running a microservice architecture, deploying dependencies can be an 
issue especially when you have two or more services sharing the same internal
dependencies.

Therefore, it makes sense to abstract them into their own internal packages
and distribute them using their various package names and  version numbers.


## How do I do this for python?
I'm running a local PyPi server using
[pypiserver](https://pypiserver.readthedocs.io/en/latest/).
This allows me to publish all my dependencies internally and manage them without
suffering over publishing multiple packages over to pypi or managing multiple package layers
which can be quite stressful in python.


Guide on getting started
---

### Installing the pypiserver 

To get this done, install the pypiserver using the dependencies
```bash
## Installation.
pip install pypiserver                ## Make it a global installation
mkdir ~/packages                      ## We'd copy packages into this directory.

## Start server.
## We won't be running this yet but you can test out the server using this
pypi-server -p 8080 ~/packages &      ## Will listen to all IPs.

```

### Configure the pypiserver to allow uploads

To enable uploads, we need to define the configuration in a pypi file and 
setup authentication for our pypiserver.

To get started with the server authentication, we are going to add passlib to
decrypt our .htaccess file. 

```bash
pip install passlib
```

We can create the .htaccess using the following command:
```bash
htpasswd -sc ~/packages/.htaccess <SOME_USERNAME>
```

After this, we're not done. We still need to configure our internal server.


### Add our internal pypiserver as a dist source

To do this, create the .pypirc file in your home directory.

This will register our internal source and we can use this later on to publish 
packages we create.

```bash
nano ~/.pypirc


## Add the following content in the file
## The username and password is the same one used in creating the .htaccess file
[distutils]
index-servers =
  internal

[internal]
repository: http://localhost:8080
username: <some_username>
password: <some_passwd>
```

To round this up, we will proceed to add the server to our pip.conf file

```bash
nano ~/.pip/pip.conf

## Add the following to the file
## You DONT need to change anything here
## You can assign a different port if that's not what your server is using
[global]
extra-index-url = http://localhost:8080/simple/

```


### Starting our server

We can finally proceed to starting our server, specifying the .htaccess file we 
created in the initial phase.

```bash
pypi-server -p 8080 -P ~/packages/.htaccess ~/packages &
```


Packaging and deploying our application on our internal PyPi server
---

### Creating the setup file

You can likewise visit [here](https://python-packaging.readthedocs.io/en/latest/minimal.html#creating-the-scaffolding)
for more indepth details on the package generation process.

```bash
## Make sure to pip install to test your setup configuration
## The filename always remains setup.py
pip install .
```


### Publishing to our pypi server

After creating the setup config, we can proceed to create distributions
of our current application.

```bash
python setup.py sdist bdist_wheel
``` 

To publish, we'd be using a tool called [twine](https://pypi.org/project/twine/)

We can use this to publish our python package.

To do so, we finalise this with

```bash
pip install twine   ## Make sure to run a global installation

## We use -r to specify the repository which we defined earlier
## before in the .pypirc file

## The dist folder contains all the code in your package [wheel and gz]
twine upload -r internal dist/*  
```

You'd see a couple logs about uploading and it should be fine.


You can view the uploaded packages by performing:

```bash
## You should see a .whl(wheel) and a .gz file
ls ~/packages/
```


# Docker Version
 - Todo section has been implemented, dev server for the pypi repository can be found in the [dev-server](dev-server) folder

## TODO:
&#x2611; - Create a docker image which would create the perfect environment

&#x2611; - It would install and run the pypiserver

- It would add the .pypirc and mount it on the local system using a volume
    
- It can build the dist and wheel and publish using a compose command



