from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from model.User import User

app = FastAPI()
engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/roach?charset=utf8mb4")
DBSession = sessionmaker(engine)
session = DBSession()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/user")
async def create_user():
    bob = User(name="spongebob", fullname="Test")
    session.add(bob)
    session.commit()

    return bob

@app.post("/user/{id}")
async def get_user(id):
    stmt = select(User).where(User.id == id)
    return session.scalar(stmt)

