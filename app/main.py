from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(
    title="My Personal Website"
)



BASE_DIR = Path(__file__).resolve().parent


# Static files (CSS, JS, Images)
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# HTML Templates
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Siavash Website",
            "message": "Welcome to my FastAPI website"
        }
    )


# Test API
@app.get("/api/test")
async def test_api():

    return {
        "status": "ok",
        "message": "FastAPI is running"
    }
