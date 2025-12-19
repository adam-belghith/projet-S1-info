from fastapi import FastAPI, Request, Query , Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from bdd.bdd import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
init_db(cur)

# --- PAGE D'ACCUEIL SIMPLE ---
@app.get("/", response_class=HTMLResponse)
def test_page(request: Request):
    # Route épurée : on affiche juste la page accueil
    return templates.TemplateResponse("acceuil.html", {"request": request})

# --- DASHBOARD (Graphiques) ---
@app.get("/dashboard", response_class=HTMLResponse)

def sensor_page(request: Request, minutes: int = Query(60)):
    time2 = int(datetime.now().timestamp())
    time1 = time2 - minutes * 60

    data_sensor = get_old_data(time1, time2)
    data_meteo = get_old_data_meteo(time1, time2)

    chart_data = {
        "sensor": {
            "ts": [row[0]*1000 for row in data_sensor],
            "temp": [row[1] for row in data_sensor],
            "humi": [row[2] for row in data_sensor],
            "co2": [row[3] for row in data_sensor]
        },
        "meteo": {
            "ts": [row[0]*1000 for row in data_meteo],
            "temp": [row[1] for row in data_meteo],
            "humi": [row[2] for row in data_meteo]
        }
    }

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "chart_data": chart_data, "minutes": minutes}
    )

# --- CONFIGURATION (Seuils) ---
@app.get("/config", response_class=HTMLResponse)
def config_page(request: Request):
    cur.execute("SELECT id, type, relation, value FROM sensor_check ORDER BY type")
    checks = cur.fetchall()
    return templates.TemplateResponse("config.html", {"request": request, "checks": checks})

@app.post("/config/add")
def add_check(type: str = Form(...), relation: str = Form(...), value: float = Form(...)):
    cur.execute("INSERT INTO sensor_check (type, relation, value) VALUES (%s, %s, %s)", (type, relation, value))
    conn.commit()
    return RedirectResponse(url="/config", status_code=303)

@app.get("/config/delete/{check_id}")
def delete_check(check_id: int):
    cur.execute("DELETE FROM sensor_check WHERE id = %s", (check_id,))
    conn.commit()
    return RedirectResponse(url="/config", status_code=303)