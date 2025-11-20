### -----------------LANCEMENT-DU-SERVEUR------------------

import uvicorn
from fastapi import FastAPI # import de la classe FastAPI
from fastapi.responses import HTMLResponse   #Bibli rendu html
from fastapi import FastAPI, Request  #Bibli templates
from fastapi.templating import Jinja2Templates #bibli templates
from fastapi.staticfiles import StaticFiles #bibli style
app = FastAPI() # Création de l application
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/action') 
def Action() -> str :
    return "Ici sera présent les différentes actions sur la rasberry."

@app.get("/consulter", response_class=HTMLResponse)
def Consulter(request:Request) -> str:
    return templates.TemplateResponse('consulter.html',{'request': request,'title':'Projet'})


@app.get('/about')
def About() -> str :
    return "Créateur : Adam, Lucas et Mathieu"

@app.get("/") # Traitement de la requête get http
def Racine() -> str: # Valeur de retour pour la réponse http
    return "bonjour tout le monde. Depuis cette page vous pouvez accèder à '/about', '/consulter', '/action'"

if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug


# Si vous ouvrez un navigateur internet à l’adresse : 
# http://127.0.0.1:8000/ vous verrez une page qui vous dit bonjour
### -------------------------------------------------------
