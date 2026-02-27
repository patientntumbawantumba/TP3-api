from pydantic import BaseModel

class AdBase(BaseModel):
    title: str
    description: str
    price: float
    location: str
    imageUrl: str | None = None

class AdCreate(AdBase):
    pass

class AdResponse(AdBase):
    id: int

    class Config:
        orm_mode = True