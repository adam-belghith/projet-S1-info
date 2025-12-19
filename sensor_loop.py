import time
from sensor.test_capteur.test_gas_humi import main2
from bdd.bdd import *
from bdd.meteo import MeteoFrance
from sensor.test_capteur.test_moteur import activer_moteur_seuil

TOKEN = "eyJ4NXQiOiJZV0kxTTJZNE1qWTNOemsyTkRZeU5XTTRPV014TXpjek1UVmhNbU14T1RSa09ETXlOVEE0Tnc9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJveHJhejkxQGNhcmJvbi5zdXBlciIsImFwcGxpY2F0aW9uIjp7Im93bmVyIjoib3hyYXo5MSIsInRpZXJRdW90YVR5cGUiOm51bGwsInRpZXIiOiJVbmxpbWl0ZWQiLCJuYW1lIjoiRGVmYXVsdEFwcGxpY2F0aW9uIiwiaWQiOjM1MzE1LCJ1dWlkIjoiYTI3OTk4ZWMtMmMzMC00NGJlLWE3ZjItYWUxNGE0MzE1MzM2In0sImlzcyI6Imh0dHBzOlwvXC9wb3J0YWlsLWFwaS5tZXRlb2ZyYW5jZS5mcjo0NDNcL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyI1MFBlck1pbiI6eyJ0aWVyUXVvdGFUeXBlIjoicmVxdWVzdENvdW50IiwiZ3JhcGhRTE1heENvbXBsZXhpdHkiOjAsImdyYXBoUUxNYXhEZXB0aCI6MCwic3RvcE9uUXVvdGFSZWFjaCI6dHJ1ZSwic3Bpa2VBcnJlc3RMaW1pdCI6MCwic3Bpa2VBcnJlc3RVbml0Ijoic2VjIn19LCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IkRvbm5lZXNQdWJsaXF1ZXNPYnNlcnZhdGlvbiIsImNvbnRleHQiOiJcL3B1YmxpY1wvRFBPYnNcL3YxIiwicHVibGlzaGVyIjoiYmFzdGllbmciLCJ2ZXJzaW9uIjoidjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiNTBQZXJNaW4ifV0sImV4cCI6MTg2MDgyMjU5NCwidG9rZW5fdHlwZSI6ImFwaUtleSIsImlhdCI6MTc2NjE0OTc5NCwianRpIjoiYmIxNDcxYWMtOTU5MC00N2FkLWI3NmEtY2EzZDA4OTM1NjBmIn0=.dxDwn6fl3gV-L-3W0bPtsjI2y0G4gKIyGGBc2lbRWl4BZWCLsS9nezGrycCMOoZCD_RpwxNJULDRqxKUX85p3ROcdp5DaST3_aEeEqnILcZSV9MdCbIZrONefl1no3b5Xc5tZbJSuR4tQzuR9aGag41_XyY_6_8v3IiC1l1Ii8rt8htmhNHr0tECeD5SOThe1Oy4KABVJTHoeU6P1viynsJBt9HVFWJFQq3_gkfkvr9BoT-XYVTgxgL2WUGtqfn4HbHb_hvW_yhscz4TMIDSHy0NOMIGLQAflfv8Ap8KxhmxFKHNadq_WTBkjttbQ0hvdIDireHDBVc8p-pF_iWvRA=="
meteo = MeteoFrance(TOKEN)

while True:
    #initialise des listes pour stocker les valeurs lues pendant 6 minutes
    # 6 minutes car l'api meteo france retourne des données toutes les 6 minutes
    l_temp = []
    l_humi = []
    l_co2 = []

    for _ in range(5):
        humi, temp, gas = main2(22,0)
        l_temp.append(temp)
        l_humi.append(humi)
        l_co2.append(gas)
        
        humi_now, temp_now, gas_now = main2(22, 0)
        cur.execute("SELECT relation, value FROM sensor_check WHERE type = 'temperature'")
        cur.execute("SELECT type, relation, value FROM sensor_check")
        regles = cur.fetchall()

        for type_capteur, relation, seuil in regles:
            # 2. On détermine quelle valeur actuelle comparer
            valeur_actuelle = None
            if type_capteur == 'temperature':
                valeur_actuelle = temp_now
            if type_capteur == 'humidity':
                valeur_actuelle = humi_now
            elif type_capteur == 'co2':
                valeur_actuelle = gas_now

            # 3. Logique de comparaison
            if valeur_actuelle is not None:
                condition_remplie = False
                if relation == ">" and valeur_actuelle > seuil:
                    condition_remplie = True
                elif relation == "<" and valeur_actuelle < seuil:
                    condition_remplie = True

                # 4. ACTION si le seuil est dépassé
                if condition_remplie:
                    activer_moteur_seuil()
                    
        time.sleep(60)

    if len(l_temp) != 0 and len(l_humi) != 0 and len(l_co2) != 0:
        # fait la moyenne des valeurs lues pendants les 6 minutes
        moyenne_temp = round(sum(l_temp) / len(l_temp), 2)
        moyenne_humi = round(sum(l_humi) / len(l_humi), 2)
        moyenne_co2 = round(sum(l_co2) / len(l_co2), 2)
        meteo_temp, meteo_humi = meteo.get_observation()

    #ajoute les valeurs dans la base de données
    if humi > 0 and temp > 0 and gas > 0:
        insert_sensor_value(moyenne_humi, moyenne_temp, moyenne_co2)
    if meteo_humi is not None and meteo_temp is not None:
        insert_meteo_value(meteo_humi, meteo_temp)
