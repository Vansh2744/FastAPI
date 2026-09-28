from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    email:str
    age:int

users:list = []

@app.post('/create')
def create(user:User):
    users.append(user)

    return {"message":"User Created"}

@app.get("/user/{id}")
def get_user(id:int):
    for user in users:
        if user.id == id:
            return user

    return {"message":"No User Found with this id"}

@app.get("/all")
def get_all():
    return users

@app.put("/user/{id}")
def update_user(id:int, user:User):
    for idx, u in enumerate(users):
        if u.id == id:
            users[idx] = user

    return users

@app.delete("/user/{id}")
def delete_user(id:int):
    for idx,u in enumerate(users):
        if u.id == id:
            users.pop(idx)

    return users