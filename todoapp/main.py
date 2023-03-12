from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def redirect_index():
    return "static/index.html"

@app.get("/hcheck", status_code=201)
def health_check():
    return ""