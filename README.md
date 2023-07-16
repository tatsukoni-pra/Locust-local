# Locust-local
Running Locust in a local environment.

# How to use
Set up environment
```
docker-compose build (Execute only the first time.)
docker-compose up -d
```

Execute Test
```
docker-compose up -d
docker exec -it python locust
```

And, access to http://localhost:8089/.
