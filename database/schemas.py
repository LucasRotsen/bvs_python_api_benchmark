from pydantic import BaseModel


class DogBase(BaseModel):
    name: str


class DogCreate(DogBase):
    pass


class Dog(DogBase):
    id: int
    name: str

    class Config:
        orm_mode = True
