from app import schemas, crud, models
from app.db import Base, engine, SessionLocal

def setup_module():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_and_get():
    db = SessionLocal()
    c = crud.create_contact(db, schemas.ContactCreate(full_name="Mario", email="mario@example.com"))
    got = crud.get_contact(db, c.id)
    assert got.email == "mario@example.com"
    db.close()
