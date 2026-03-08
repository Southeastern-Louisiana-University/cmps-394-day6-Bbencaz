from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class UserBase(BaseModel):
    username: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# POST - create user
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserBase, db: db_dependency):
    new_user = models.User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET - get all users
@app.get("/users")
def get_users(db: db_dependency):
    users = db.query(models.User).all()
    return users


# DELETE - delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
