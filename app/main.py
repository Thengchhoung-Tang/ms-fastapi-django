from fastapi import FastAPI
import pathlib
from fastapi import templating
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR /"templates"))


@app.get('/', response_class=HTMLResponse)
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "abc": 123})


@app.post('/')
def home_view():
    return {"Hello": "world"}