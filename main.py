from fastapi import FastAPI

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