from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    
    name  : str    
    age : int 
    weight : float #kg
    height : float #mtr
    married : bool = False # default value is False
    allergies : Optional[List[str]] = Field(max_length=5)
    contact_details : Dict[str, str]
    email : EmailStr

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi
    
def insert_patient_data(patient : Patient): # type hinting

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.height)
    print(patient.allergies)
    print("BMI", patient.bmi)
    print(f"Patient Contact Details: {patient.contact_details}")
    print("Update")

patient_info = {'name' : 'dhaval', 'age' : '72', 'email' : 'asdfghjjkl@sap.com', 'weight' : '90.0', 'height' : '1.8000','married': True, 'allergies' : ['polen', 'dust'], 'contact_details' : {'emergency' : '17657936527', }}

patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)
