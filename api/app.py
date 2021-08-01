from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from service import dogs
from database.config import engine
from api.dependencies import get_db
from database import models, schemas
from api.config import ALLOWED_ORIGINS

app = FastAPI(
    title='BVS Benchmark | Python',
    description='Python API for benchmark',
    version='0.0.1',
    docs_url='/documentation',
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=ALLOWED_ORIGINS
)

models.Base.metadata.create_all(bind=engine)


@app.post("/dogs/", response_model=schemas.Dog)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    db_dog = dogs.get_dog_by_name(db, name=dog.name)
    if db_dog:
        raise HTTPException(status_code=400, detail="Dog name already registered")
    return dogs.create_dog(db=db, dog=dog)


@app.get("/dogs/", response_model=List[schemas.Dog])
def read_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doggos = dogs.get_dogs(db, skip=skip, limit=limit)
    return doggos


@app.get("/dogs/{dog_id}", response_model=schemas.Dog)
def read_dog(dog_id: int, db: Session = Depends(get_db)):
    db_dog = dogs.get_dog(db, dog_id=dog_id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog


@app.delete("/dogs/")
def delete_dog(dog_id: int, db: Session = Depends(get_db)):
    db_dog = dogs.delete_dog(db, dog_id=dog_id)
    return db_dog


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
