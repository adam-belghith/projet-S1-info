# Se placer dans le dossier du projet
cd /home/raspi/Desktop/projet/projetV2/bdd 

# Variables
CONTAINER_NAME=postgres
POSTGRES_PASSWORD=password
DB_NAME=projet
DB_USER=username
DB_PASSWORD=password
IMAGE=docker.io/postgres:17


podman run --name $CONTAINER_NAME -d --rm \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  --network=host \
  $IMAGE

# Attendre que PostgreSQL soit prêt
sleep 10

podman exec -u postgres $CONTAINER_NAME createdb $DB_NAME

podman exec -u postgres $CONTAINER_NAME psql -c "
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
ALTER DATABASE $DB_NAME OWNER TO $DB_USER;
"

cd /home/raspi/Desktop/projet/projetV2
uvicorn api:app --reload --host 0.0.0.0 --port 8000