from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str 
    age : Optional[int] = None
    # email : EmailStr ## Built-in validation is available (, 'email' : "abc@gmail.com")
    cgpa : float = Field(gt = 0, lt=10.01, default=5, description=" A decimal value representing the cgpa of the student")


new_student = {'name' : "Dhaval", 'age' : 27, 'cgpa' : 10}


student = Student(**new_student)

student_dict = dict(student)

print(student_dict)


studnet_json = student.model_dump_json()

studnet_json = student.model_dump_json()
print(studnet_json)