from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define a data model
class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage
items_db = []

# TODO: Implement GET endpoint to retrieve all items
@app.get("/items", response_model=List[Item])
async def get_items():
    pass

# TODO: Implement GET endpoint to retrieve a single item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    pass

# TODO: Implement POST endpoint to create a new item
@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    pass

# TODO: Implement PUT endpoint to update an item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    pass

# TODO: Implement DELETE endpoint to remove an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    pass
