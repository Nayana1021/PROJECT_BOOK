from app.database import collection
from app.schemas import Item
from bson import ObjectId

def create_item(item: Item):
    new_item = item.dict()
    result = collection.insert_one(new_item)
    created_item = collection.find_one({"_id": result.inserted_id})
    
    # Return the created item with the _id converted to a string
    return {
        "id": str(created_item["_id"]),  # Convert ObjectId to string
        "name": created_item["name"],
        "description": created_item["description"],
        "price": created_item["price"]
    }

def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    return item

def get_all_items():
    items = collection.find()
    return [item for item in items]

def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count == 1
