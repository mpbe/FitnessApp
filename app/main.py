from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, workouts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#create the database tables
Base.metadata.create_all(bind=engine)

#add CORS middleware to help integration with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#register the routers when created
app.include_router(users.router)
app.include_router(workouts.router)

@app.get("/")
def homepage():
    return {"message": "head to /docs to preview the app's core functionality"}