from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        json_data = json.load(file)

        return json_data

@app.get("/")
async def hello():
    return {"message": "Patient Management System API"}

@app.get("/doctor")
async def dhaval():
    return {"message": "Dr. Dhaval MBBS, MD (General Medicine)"}

@app.get("/about")
async def about():
    return {"message": "A fully functional Patient Management System API built with FastAPI. It includes endpoints for managing patients, appointments, and medical records."}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description="The ID of the patient in the DB", example="P001")):
    data = load_data()
    print(f"Fetching data for patient ID: {patient_id}")
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort basis of height, weight or bmi"), order:str = Query('asc', description= 'sort of asc or desc order.'), ):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'.")
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data