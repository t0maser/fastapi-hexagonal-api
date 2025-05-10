# This module contains the API adapters for the application.

from fastapi import APIRouter
from application.services import get_item_details

router = APIRouter()

@router.get("/items/{name}")
def read_item(name: str):
    item = get_item_details(name)
    return {"name": item.name, "description": item.description}