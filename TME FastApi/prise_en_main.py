import uvicorn   #Bibli intro
from fastapi import FastAPI  #Bibli intro
from fastapi.responses import HTMLResponse   #Bibli rendu html
from fastapi import FastAPI, Request  #Bibli templates
from fastapi.templating import Jinja2Templates #bibli templates
from fastapi.staticfiles import StaticFiles #bibli style
app = FastAPI() # Création de l application
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def hello(request:Request) -> str:
    user = {'username': 'Cécile'}
    return templates.TemplateResponse('hello.html',{'request': request,'title':'First page', 'user':user})


@app.get("/petit_dej", response_class=HTMLResponse)
def petit_dej(request:Request) -> str:
    return templates.TemplateResponse('Ex1_HiChart_copie.html',{'request': request})

if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug


#La page des petit dej :            http://127.0.0.1:8000/petit_dej


