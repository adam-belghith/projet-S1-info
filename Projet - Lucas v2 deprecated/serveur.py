###----------LANCEMENT-DE-SQLITE--------------------------
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database 
    Return a pointer to the open connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
###-------------------------------------------------------


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



@app.get('/action', response_class=HTMLResponse) 
def Action(request:Request) -> str :
    return templates.TemplateResponse('action.html',{'request': request,'title':'Projet'})

@app.get("/consulter", response_class=HTMLResponse)
def Consulter(request:Request) -> str:

    ### TRUC DU PROF ###
    #open the SQLite database
    connection = create_connection("./test.db") 
    #execute a query
    cur = connection.cursor()
    cur.execute("SELECT * FROM ARTICLE")
    #print results
    results = cur.fetchall()
    ###--------------###
    
    data = str(results[0][0])
    return templates.TemplateResponse('consulter.html',{'request': request,'title':'Projet', 'data': data})


@app.get('/about')
def About() -> str :
    return "Créateur : Adam, Lucas et Mathieu"

@app.get("/", response_class=HTMLResponse) # Traitement de la requête get http
def Racine(request:Request) -> str: # Valeur de retour pour la réponse http
    return templates.TemplateResponse('ecran_d_aceuil.html',{'request': request,'title':'Projet'})
    
if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug


# Si vous ouvrez un navigateur internet à l’adresse : 
# http://127.0.0.1:8000/ vous verrez une page qui vous dit bonjour
### -------------------------------------------------------
