import bdd.main
import notifications.main

def test():
    bdd.main.add_push_notif("humidity", ">", 60, 1, "https://ntfy.sh/ogkebfjelfktieo")
    bdd.main.insert_sensor_value(humidity=80)
    notifications.main.verif_notifs("humidity", 80)

test()