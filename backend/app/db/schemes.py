from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class StudentCreate(StudentBase):
    pass

class StudentPublic(StudentBase):
    id: str

class StudentUpdate(BaseModel):
    pass


