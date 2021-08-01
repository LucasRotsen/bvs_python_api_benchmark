from sqlalchemy.orm import Session

from database import models, schemas


def get_dog(db: Session, dog_id: int):
    return db.query(models.Dog).filter(models.Dog.id == dog_id).first()


def get_dog_by_name(db: Session, name: str):
    return db.query(models.Dog).filter(models.Dog.name == name).first()


def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dog).offset(skip).limit(limit).all()


def create_dog(db: Session, dog: schemas.DogCreate):
    db_dog = models.Dog(name=dog.name)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog


def delete_dog(db: Session, dog_id: int):
    db_dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    return db_dog
