from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Algoritmo funcionando"}

@app.get("/extraer")
def extraer(usuario: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    url = f"https://www.tiktok.com/api/v1/user/detail/?uniqueId={usuario}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json()
    except:
        return {"error": "No se pudo conectar"}
