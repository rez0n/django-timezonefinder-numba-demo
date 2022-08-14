
## Pre requirements
You need to have installed in your system
* Python 3.9
* poetry
* Docker
* docker-compose

## Install Python packages
```
poetry env use python3.9
poetry shell
poetry install
```

## Run locally
```
python manage.py runserver 127.0.0.1:8081
```
#### Open locally started instance
[http://localhost:8081](http://localhost:8081)


## Run in-Docker instance
```
docker-compose up --build
```
#### Open Docker instance
[http://localhost:8082](http://localhost:8082)


## Raw script

### Execute locally
```
python test.py
```

### Execute in Docker
```
docker-compose up raw_script --build
```

It will continuously run again and again if `restart: always` is set in docker-compose.yml