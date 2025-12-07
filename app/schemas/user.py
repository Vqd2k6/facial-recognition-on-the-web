from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username: str
    password: str
    image_base64: str

class LoginRequest(BaseModel):
    username: str
    password: str
    image_base64: str