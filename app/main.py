from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, workouts

app = FastAPI()

#create the database tables
Base.metadata.create_all(bind=engine)

#register the routers when created
app.include_router(users.router)
app.include_router(workouts.router)

@app.get("/")
def homepage():
    return {"message": "API is running"}