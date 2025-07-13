from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    
    name  : str    
    age : int 
    weight : float
    married : bool = False # default value is False
    allergies : Optional[List[str]] = Field(max_length=5)
    contact_details : Dict[str, str]
    email : EmailStr


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'sap.com']
        # dhaval@sap.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid Domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

    
def insert_patient_data(patient : Patient): # type hinting

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(f"Patient Contact Details: {patient.contact_details}")
    print("Update")

patient_info = {'name' : 'dhaval', 'age' : '27', 'email' : 'asdfghjjkl@sap.com', 'weight' : '90.0', 'married': True, 'allergies' : ['polen', 'dust'], 'contact_details' : {'mobile' : '17657936527', }}

patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)
