# mongodb-python-connects
Sobre script python con conexión a Atlas-MongoDB


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
