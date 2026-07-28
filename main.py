from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="InitSpace")

BASE_DIR = Path(__file__).resolve().parent
# Static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


# HTML Templates
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


TUTORIALS = [
    {
        "slug": "zabbix-agent2-setup",
        "title": "How to Deploy Zabbix Agent 2 on Linux",
        "tag": "Zabbix",
        "date": "2026-07-25",
        "summary": "Step-by-step guide to installing Zabbix Agent 2, configuring encrypted PSK communication, and custom metric collection.",
        "content": """
            <h2>Introduction</h2>
            <p>Zabbix Agent 2 is written in Go and provides high-performance metric collection for modern Linux infrastructures.</p>
            <h3>Step 1: Install Zabbix Repository</h3>
            <pre><code>wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_latest+ubuntu24.04_all.deb
dpkg -i zabbix-release_latest+ubuntu24.04_all.deb
apt update</code></pre>
            <h3>Step 2: Install Agent 2</h3>
            <pre><code>apt install zabbix-agent2</code></pre>
        """
    },
    {
        "slug": "zabbix-postgresql-partman_1",
        "title": "How to Install Zabbix 7.0 LTS with PostgreSQL 14 & pg_partman",
        "tag": "Zabbix & PostgreSQL",
        "date": "2026-07-28",
        "summary": "Enterprise guide to configuring Zabbix 7.0 LTS with PostgreSQL native range partitioning for zero-IO database cleanup.",
        "template_name": "zabbix_tutorial_1.html",
    }
]


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "title": "InitSpace",
            "message": "Welcome to my FastAPI website",
            "tutorials": TUTORIALS
        }
    )

# Single Tutorial Page (Dynamic Routing)
@app.get("/tutorials/{slug}", response_class=HTMLResponse)
async def read_tutorial(request: Request, slug: str):
    tutorial = next((item for item in TUTORIALS if item.get("slug") == slug), None)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")

    if "template_name" in tutorial:
        return templates.TemplateResponse(
            request=request,
            name=tutorial["template_name"],
            context={"request": request}
        )

    return templates.TemplateResponse(
        request=request,
        name="tutorial_detail.html",
        context={
            "request": request,
            "title": tutorial["title"],
            "tag": tutorial["tag"],
            "date": tutorial["date"],
            "content": tutorial.get("content", "")
        }
    )
