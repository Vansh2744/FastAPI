from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    name:str
    email:str

# @app.get("/user", response_model=UserResponse)
# def get_user():
#     return {
#         'name':'Vansh',
#         'email':'vansh@gmail.com',
#         'password':'vk2744ok'
#     }

# @app.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# def create(user:User):
#     return user

@app.get("/user", response_model=UserResponse)
def get_user():
    # user = {'name':"Vansh",'email':"vansh@gmail.com"}
    user = None
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")