# test on : http://127.0.0.1:8000
# Run by : uvicorn main:app --reload
#CD to file main.py before run script
from fastapi import FastAPI
from routes import item

app = FastAPI()

app.include_router(item.router)

@app.get("/")
def read_root():
    return {"messae" : "Hello pung yoop api"}