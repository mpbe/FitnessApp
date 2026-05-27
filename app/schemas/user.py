from pydantic import BaseModel, EmailStr


"""
Request JSON
↓
UserCreate validates input
↓
Router receives UserCreate object
↓
Password hashed
↓
User saved to DB
↓
UserOut formats response
↓
Response returned
"""

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
