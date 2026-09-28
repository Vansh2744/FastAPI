from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return {'name':'Vansh', 'email':'vansh@gmail.com'}

@app.get('/current-user')
async def current_user():
    return {'id':'yetr643r6346rt46r64r4rr4', 'email':'vansh@gmail.com', 'age':23}