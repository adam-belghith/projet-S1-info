import requests
# Votre token qui fonctionne
TOKEN = "eyJ4NXQiOiJZV0kxTTJZNE1qWTNOemsyTkRZeU5XTTRPV014TXpjek1UVmhNbU14T1RSa09ETXlOVEE0Tnc9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJveHJhejkxQGNhcmJvbi5zdXBlciIsImFwcGxpY2F0aW9uIjp7Im93bmVyIjoib3hyYXo5MSIsInRpZXJRdW90YVR5cGUiOm51bGwsInRpZXIiOiJVbmxpbWl0ZWQiLCJuYW1lIjoiRGVmYXVsdEFwcGxpY2F0aW9uIiwiaWQiOjM1MzE1LCJ1dWlkIjoiYTI3OTk4ZWMtMmMzMC00NGJlLWE3ZjItYWUxNGE0MzE1MzM2In0sImlzcyI6Imh0dHBzOlwvXC9wb3J0YWlsLWFwaS5tZXRlb2ZyYW5jZS5mcjo0NDNcL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyI1MFBlck1pbiI6eyJ0aWVyUXVvdGFUeXBlIjoicmVxdWVzdENvdW50IiwiZ3JhcGhRTE1heENvbXBsZXhpdHkiOjAsImdyYXBoUUxNYXhEZXB0aCI6MCwic3RvcE9uUXVvdGFSZWFjaCI6dHJ1ZSwic3Bpa2VBcnJlc3RMaW1pdCI6MCwic3Bpa2VBcnJlc3RVbml0Ijoic2VjIn19LCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IkRvbm5lZXNQdWJsaXF1ZXNPYnNlcnZhdGlvbiIsImNvbnRleHQiOiJcL3B1YmxpY1wvRFBPYnNcL3YxIiwicHVibGlzaGVyIjoiYmFzdGllbmciLCJ2ZXJzaW9uIjoidjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiNTBQZXJNaW4ifV0sImV4cCI6MTg2MDgyMjU5NCwidG9rZW5fdHlwZSI6ImFwaUtleSIsImlhdCI6MTc2NjE0OTc5NCwianRpIjoiYmIxNDcxYWMtOTU5MC00N2FkLWI3NmEtY2EzZDA4OTM1NjBmIn0=.dxDwn6fl3gV-L-3W0bPtsjI2y0G4gKIyGGBc2lbRWl4BZWCLsS9nezGrycCMOoZCD_RpwxNJULDRqxKUX85p3ROcdp5DaST3_aEeEqnILcZSV9MdCbIZrONefl1no3b5Xc5tZbJSuR4tQzuR9aGag41_XyY_6_8v3IiC1l1Ii8rt8htmhNHr0tECeD5SOThe1Oy4KABVJTHoeU6P1viynsJBt9HVFWJFQq3_gkfkvr9BoT-XYVTgxgL2WUGtqfn4HbHb_hvW_yhscz4TMIDSHy0NOMIGLQAflfv8Ap8KxhmxFKHNadq_WTBkjttbQ0hvdIDireHDBVc8p-pF_iWvRA=="
url = "https://public-api.meteofrance.fr/public/DPObs/v1/station/infrahoraire-6m"

headers = {
    "apikey": TOKEN, 
    "accept": "*/*"
}

params = {
    "id_station": "75114001",
    "format": "json"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # Accès aux données
    try:
        mesure = data[0]
            
        t_kelvin = mesure.get('t')
        humi = mesure.get('u')
        
        t_celsius = round(t_kelvin - 273.15, 2)
    except Exception as e:
        pass

class MeteoFrance:
    def __init__(self, token):
        self.token = token
        self.url = "https://public-api.meteofrance.fr/public/DPObs/v1/station/infrahoraire-6m"

    def get_observation(self, station_id="75114001"):
        headers = {"apikey": self.token, "accept": "application/json"}
        params = {"id_station": station_id, "format": "json"}
        try:
            response = requests.get(self.url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                mesure = data[0] if isinstance(data, list) else data
                temp_k = mesure.get('t')
                temp_c = round(temp_k - 273.15, 2) if temp_k is not None else None
                return (temp_c, mesure.get('u'))
        except:
            pass
        return (0, 0)