from fastapi import APIRouter, HTTPException
from app.schemas import Item
from app.crud import create_item, get_item, get_all_items, delete_item

router = APIRouter()

@router.post("/items/", response_model=dict)
async def create_item_route(item: Item):
    created_item = create_item(item)
    return created_item

@router.get("/items/{item_id}", response_model=dict)
async def read_item_route(item_id: str):
    item = get_item(item_id)
    if item:
        return {
            "id": str(item["_id"]),  # Convert ObjectId to string
            "name": item["name"],
            "description": item["description"],
            "price": item["price"]
        }
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/", response_model=list)
async def read_items_route():
    items = get_all_items()
    
    # Construct the response for multiple items
    return [
        {
            "id": str(item["_id"]),  # Convert ObjectId to string
            "name": item["name"],
            "description": item["description"],
            "price": item["price"]
        } for item in items
    ]

@router.delete("/items/{item_id}", response_model=dict)
async def delete_item_route(item_id: str):
    if delete_item(item_id):
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
