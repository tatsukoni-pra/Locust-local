# Locust-local
Running Locust in a local environment.

# How to use
Set up environment
```
docker-compose build (Execute only the first time.)
docker-compose up -d
docker exec -it python sh
```

Execute Test
```
docker exec -it python locust
Access to http://localhost:8089/
```
