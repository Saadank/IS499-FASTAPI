from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/login", response_class=HTMLResponse, name="login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/signup", response_class=HTMLResponse, name="signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})
