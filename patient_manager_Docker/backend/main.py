from fastapi import FastAPI, HTTPException, Path
from models import Patient
from database import patient_collection
from bson import ObjectId

app = FastAPI()

#Fix: Add CORS Middleware in FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/create")
async def create_patient(patient: Patient):
    if await patient_collection.find_one({"id": patient.id}):
        raise HTTPException(status_code=400, detail="Patient already exists")

    await patient_collection.insert_one(patient.model_dump())
    return {"message": "Patient created successfully"}

@app.get("/view")
async def view_all():
    patients = []
    async for patient in patient_collection.find():
        patient["_id"] = str(patient["_id"])  # ✅ Fix ObjectId issue
        patients.append(patient)
    return patients

@app.get("/patient/{patient_id}")
async def get_patient(patient_id: str):
    patient = await patient_collection.find_one({"id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient["_id"] = str(patient["_id"])  # ✅ Fix ObjectId issue
    return patient


@app.put("/edit/{patient_id}")
async def update_patient(patient_id: str, update: dict):
    result = await patient_collection.update_one({"id": patient_id}, {"$set": update})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient updated"}

@app.delete("/delete/{patient_id}")
async def delete_patient(patient_id: str):
    result = await patient_collection.delete_one({"id": patient_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted"}
