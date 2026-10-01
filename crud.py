from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/all", response_model=list[UserResponse])
def get_all(db:Session = Depends(get_db)):
    users = db.query(models.User).all()

    return users

@app.get("/user/{id}", response_model=UserResponse)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return user

@app.put('/user/{id}', response_model=UserResponse)
def update_user(id:int, updated_user:UserCreate, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    user.name = updated_user.name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    return user

@app.delete("/user/{id}")
def delete_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    db.delete(user)

    db.commit()

    return {
        "message":"User Deleted Successfully"
    }