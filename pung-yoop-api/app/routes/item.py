from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name : str

items = []

@router.get("/items")
def get_items():
    return items

@router.post("/items")
def create_item(items: Item):
    items.append(item)
    return {"messgr" : "Item addd", "data" : item}