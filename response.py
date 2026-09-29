from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    name:str
    email:str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        'name':'Vansh',
        'email':'vansh@gmail.com',
        'password':'vk2744ok'
    }