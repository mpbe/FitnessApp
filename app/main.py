from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

#create the database tables
Base.metadata.create_all(bind=engine)

#register the routers when created

@app.get("/")
def homepage():
    return {"message": "API is running"}