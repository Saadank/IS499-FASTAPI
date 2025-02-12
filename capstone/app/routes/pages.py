from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse, name="home")
async def home(request: Request):
    return templates.TemplateResponse("landingpage.html", {"request": request})

@router.get("/auction", response_class=HTMLResponse, name="auction")
async def auction_page(request: Request):
    return templates.TemplateResponse("auction.html", {"request": request})

@router.get("/forsale", response_class=HTMLResponse, name="forsale")
async def for_sale_page(request: Request):
    return templates.TemplateResponse("forsale.html", {"request": request})


