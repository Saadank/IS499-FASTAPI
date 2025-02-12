from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Form
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/login", response_class=HTMLResponse, name="login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    # Replace with real authentication logic
    if username == "admin" and password == "password":
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@router.get("/signup", response_class=HTMLResponse, name="signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup")
async def signup_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    # Replace with actual signup logic (e.g., save to database)
    return {"message": f"User {username} signed up successfully"}
