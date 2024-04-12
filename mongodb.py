from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

def connect_to_atlas():
    connection_url = os.environ.get("MONGODB_URL")
    try:
        client = pymongo.MongoClient(connection_url)
        print("Connected to MongoDB Atlas successfully!")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print("Connection error:", e)
        return None


mongodb = connect_to_atlas()

if mongodb is None:
    exit(1)
