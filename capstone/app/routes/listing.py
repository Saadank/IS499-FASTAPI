from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/addlisting", response_class=HTMLResponse, name="addlisting")
async def add_listing(request: Request):
    return templates.TemplateResponse("addlisting.html", {"request": request})

