# mongodb-python-connects
Sobre script python con conexión a Atlas-MongoDB.

Dockeriza el script y lo pushea a DockerHub mediante GitHub Actions al hacer un push a main.


## Para conectarse al cli de Mongodb

*prerequisitos*

- brew install mongodb-atlas-cli

- atlas auth login

- atrlas setup


Commands:

```console
mongosh "mongodb+srv://Cluster78180:fHtlpirulines@cluster78180.mwv8wrj.mongodb.net" --apiVersion 1 --username Cluster78180
```

## Dockerizar


```console
docker build -t mongoconnect .
```
```console
docker run mongoconnect
```

## Github Actions

https://github.com/nicosistemas/mongodb-python-connects/blob/main/.github/workflows/actions.yml

## Docker Hub

https://hub.docker.com/repository/docker/nicosistemas/mongoconnect/general
