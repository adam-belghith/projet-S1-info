Il faut lancer postgresql à côté, et en mettant la config dans env.py en suivant le modèle de env.example.py

Pour le dev :
```
sudo apt install podman uidmap
podman run --name postgres -d --rm -e POSTGRES_PASSWORD=password --network=host docker.io/postgres:17
podman exec -it -u postgres postgres createdb projet
podman exec -it -u postgres postgres psql -c "CREATE USER username WITH password 'password'; GRANT all privileges ON database projet TO username; ALTER DATABASE projet OWNER to username;"
```