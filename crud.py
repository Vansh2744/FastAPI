from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
from schemas import UserCreate, UserResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/create", response_model=UserResponse)
def create(user:UserCreate, db:Session=Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email, password=user.password)

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user