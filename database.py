from pymongo import MongoClient

# MongoDB connection configuration
client = MongoClient("mongodb://localhost:27017")
db = client["books_db"]
collection = db["books"]
