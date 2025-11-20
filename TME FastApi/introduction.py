### -----------------LANCEMENT-DU-SERVEUR------------------

import uvicorn
from fastapi import FastAPI # import de la classe FastAPI
app = FastAPI() # Création de l application


@app.get('/about') #Sous-page que j'ai rajouté
def truc_bidule() -> str :
    return "Ceci est un descriptif"

@app.get("/") # Traitement de la requête get http
def machin_bidule() -> str: # Valeur de retour pour la réponse http
    return "bonjour tout le monde"

if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug


# Si vous ouvrez un navigateur internet à l’adresse : 
# http://127.0.0.1:8000/ vous verrez une page qui vous dit bonjour
### -------------------------------------------------------



