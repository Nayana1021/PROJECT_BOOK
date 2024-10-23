from fastapi import FastAPI
from app.routes import item_routes

app = FastAPI()

# Include the item routes
app.include_router(item_routes.router)

# Optional: Add this if you want to run the server from this script
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
