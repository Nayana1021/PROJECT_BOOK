# My FastAPI Project

This is a simple FastAPI project that interacts with MongoDB to manage items.

## Setup

1. Clone the repository: git clone https://github.com/Nayana1021/PROJECT_BOOK
2. Install the requirements: pip install -r requirements.txt
3. Run the application: uvicorn app.main:app --reload

## API Endpoints

- `POST /items/`: Create a new item.
- `GET /items/{item_id}`: Get an item by ID.
- `GET /items/`: Get all items.
- `DELETE /items/{item_id}`: Delete an item by ID.
