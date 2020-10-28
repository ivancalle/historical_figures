# Historical figures API

This software is an API that implements a CRUD of historical figures

## Requirements

### Without docker

You need to have python >= 3.8 (https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/) and pip >= 20.2 (https://pip.pypa.io/en/stable/installing/).

Then you need to intall the project's requirements and the project, you can do with command:
```
$pip install -r requirements/install.txt .
```

If you want to run the test then you need intall the test's requirements with command:

```
$pip install -r requirements/test.txt
```

You need a mongodb server for the application works correctly.

### With docker

You need to have docker >= 19.03.9 (https://docs.docker.com/engine/install/ubuntu/) and it is recommended use docker-compose>=1.17 (https://docs.docker.com/compose/install/).


## Execute

### Without docker

You need export the variable MONGODB_DSN with the dsn of mongo server, for example:

```
$export MONGODB_DSN=mongodb://localhost/figures
```

For execute the app you need execute next command:

```
$python -m figures --debug serve
```

--debug option is mainly for dont use logsfiles, if you dont put this option, the app crash because dont find the logfiles.


### With docker-compose

You only need execute:

```
$docker-compose up python-test
```

## API docs

If you want to see the API docs you can go to http://localhost:8000/docs (or :8080 with docker).
