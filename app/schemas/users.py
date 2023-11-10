from pydantic import BaseModel, EmailStr


class UserEmail(BaseModel):
    email: EmailStr

class UserInfoEmail(UserEmail):
    message: str