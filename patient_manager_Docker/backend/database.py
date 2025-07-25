import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")

client = AsyncIOMotorClient(MONGO_URL)
db = client.patientdb
patient_collection = db["patients"]

