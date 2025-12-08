import requests
import bdd.main

def envoyer_notification(message, url):
    requests.post(str(url), data = str(message).encode(encoding='utf-8'))

def verif_notifs(type, valeur):
    bdd.main.cur.execute(f"select * FROM sensor_check WHERE type='{type}'")
    for tuple_check in bdd.main.cur.fetchall():
        if tuple_check[2] == ">":
            if valeur > tuple_check[3]:
                bdd.main.cur.execute(f"select * FROM push_notification WHERE sensor_check_id={tuple_check[0]}")
                liste_url = bdd.main.cur.fetchall()
                for tuple_url in liste_url:
                    envoyer_notification(f"{type} : {valeur}", tuple_url[2])
        elif tuple_check[2] == "<":
            if valeur < tuple_check[3]:
                bdd.main.cur.execute(f"select * FROM push_notification WHERE sensor_check_id={tuple_check[0]}")
                liste_url = bdd.main.cur.fetchall()
                for tuple_url in liste_url:
                    envoyer_notification(f"{type} : {valeur}", tuple_url[2])


