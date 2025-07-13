from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    
    name  : str    
    age : int 
    weight : float
    married : bool = False # default value is False
    allergies : Optional[List[str]] = Field(max_length=5)
    contact_details : Dict[str, str]
    email : EmailStr


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older than 60 please emergency contact")
    

    
def insert_patient_data(patient : Patient): # type hinting

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(f"Patient Contact Details: {patient.contact_details}")
    print("Update")

patient_info = {'name' : 'dhaval', 'age' : '72', 'email' : 'asdfghjjkl@sap.com', 'weight' : '90.0', 'married': True, 'allergies' : ['polen', 'dust'], 'contact_details' : {'emergency' : '17657936527', }}

patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)
