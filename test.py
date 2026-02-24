from pymongo import MongoClient

client = MongoClient("mongodb+srv://shailesh:Shailesh123@cluster0.fkkg9xb.mongodb.net/?appName=Cluster0")

db = client["school"]
collection = db["students"]

print("✅ Connected Successfully!")