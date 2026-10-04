from fastapi import FastAPI, Depends, HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone

load_dotenv()

app = FastAPI()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp":expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

@app.post('/login')
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    if form_data.email not in ['vansh@gmail.com', 'aman@gmail.com']:
        raise HTTPException(status_code=401, detail="Invalid Email")

    if not verify_password(form_data.password, "$2b$12$.a0o5hZqehVe0UwZVDlC3eCPkX4IsU2tuW4Y0L0voCZHt61PRdXNa"):
        raise HTTPException(status_code=401, detail="Invalid Password")

    token = create_access_token({'email':form_data.email})

    return {'token':token}