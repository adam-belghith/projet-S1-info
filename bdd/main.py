import psycopg2
from datetime import datetime
from env import *

conn = psycopg2.connect(database = PG_DB,
                        user = PG_USER,
                        host= PG_HOST,
                        password = PG_PASSWORD,
                        port = PG_PORT)
cur = conn.cursor()


def check_if_empty()-> bool:
    '''
        Copié d'ici https://stackoverflow.com/questions/10598002/how-do-i-get-tables-in-postgres-using-psycopg2
    '''
    cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    return bool(cur.fetchone())


def reset_db():
    cur.execute("DROP TABLE IF EXISTS sensor_check;")
    cur.execute("DROP TABLE IF EXISTS push_notification;")
    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("DROP TABLE IF EXISTS sensor;")
    conn.commit()




def init_db(cur):
    if check_if_empty():
        return -1
    cur.execute("CREATE TABLE users (id int NOT NULL,username varchar NOT NULL,password_hash varchar,PRIMARY KEY (id));")
    cur.execute("CREATE TABLE push_notification (id int NOT NULL,user_id int NOT NULL,url varchar,sensor_check varchar,PRIMARY KEY (id),FOREIGN KEY (user_id) REFERENCES users(id));")
    cur.execute("CREATE TABLE sensor_check (id int NOT NULL,type varchar,relation varchar,value float,PRIMARY KEY (id));")
    cur.execute("CREATE TABLE sensor (time int,temperature float,humidity float,co2 float);")
    conn.commit()




def insert_sensor_value(humidity=None, temperature=None, co2=None):
    time = int(datetime.now().timestamp())
    # On part du principe qu'il n'y a pas 2 requêtes pour la même secondes, et qu'il y a au moins une des 3 valeurs
    str_columns = ""
    str_values = ""
    if humidity :
        str_columns = ", humidity"
        str_values = ", " + str(humidity)
    if temperature :
        str_columns += ", temperature"
        str_values += ", " + str(temperature)
    if co2:
        str_columns += ", co2"
        str_values += ", " + str(co2)

    # Pour retirer la première virgule
    str_columns = str_columns[1:len(str_columns)]
    str_values = str_values[1:len(str_values)]

    cur.execute(f"INSERT INTO sensor (time, {str_columns}) VALUES ({time}, {str_values});")
    conn.commit()

def get_old_data(time1, time2):
    '''
        Renvoie une liste qui contient des tuples (time, temperature, humidity, co2), avec des None quand il n'y a pas de valeur
    '''
    cur.execute(f"SELECT * FROM sensor WHERE time > {time1} and time < {time2};")
    return cur.fetchall()

init_db(cur)
