from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def home():
    return {'name':'Vansh', 'email':'vansh@gmail.com'}

@app.get('/current-user')
async def current_user():
    return {'id':'yetr643r6346rt46r64r4rr4', 'email':'vansh@gmail.com', 'age':23}

# Dynamic Route(Path Parameter)
@app.get('/user/{id}')
async def get_user(id:str):
    return {'message':f'Fetch User with id : {id}'}

# Query Parameter
@app.get('/user-by-name')
def user_by_name(name):
    return {'name':name}

@app.get('/user-info')
def get_info(name:str = None, email:str = None):
    return {'name':name, 'email':email}

# @app.post('/create')
# def create(name:str=Form(...), email:str=Form(...)):
#     return {'name':name, 'email':email}

# @app.post('/create')
# def create(user:dict):
#     return user

class User(BaseModel):
    name:str
    email:str
    age:int

@app.post('/create')
def create(user:User):
    return user

# Path + Query + Body
@app.post('/combo/{id}')
def get_combo(id:int, user:User, sex:str):
    return {'id':id, 'sex':sex, 'data':user}