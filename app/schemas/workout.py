from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    name: str
    description: str


class WorkoutOut(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes=True
