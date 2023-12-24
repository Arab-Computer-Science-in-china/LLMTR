from fastapi import FastAPI
from api import Start

app = FastAPI()
app.include_router(Start.router)
