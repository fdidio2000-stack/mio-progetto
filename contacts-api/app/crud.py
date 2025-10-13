import logging
from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

logger = logging.getLogger(__name__)

def create_contact(db: Session, data: schemas.ContactCreate) -> models.Contact:
    logger.debug(f"Creating contact with data: {data}")
    try:
        c = models.Contact(
            full_name=data.full_name,
            email=str(data.email),
            phone=data.phone,
            tags=data.tags or []
        )
        db.add(c)
        db.commit()
        db.refresh(c)
        logger.debug(f"Contact created successfully: {c}")
        return c
    except Exception as e:
        logger.exception(f"Failed to create contact: {e}")
        db.rollback()
        raise


def get_contact(db: Session, cid: int):
    logger.debug(f"Fetching contact with ID: {cid}")
    try:
        contact = db.get(models.Contact, cid)
        logger.debug(f"Fetched contact: {contact}")
        return contact
    except Exception as e:
        logger.exception(f"Error fetching contact by ID {cid}: {e}")
        raise


def get_by_email(db: Session, email: str):
    logger.debug(f"Fetching contact by email: {email}")
    try:
        result = db.execute(
            select(models.Contact).where(models.Contact.email == email)
        ).scalar_one_or_none()
        logger.debug(f"Fetched by email result: {result}")
        return result
    except Exception as e:
        logger.exception(f"Error fetching contact by email {email}: {e}")
        raise


def update_contact(db: Session, c: models.Contact, patch: schemas.ContactUpdate):
    logger.debug(f"Updating contact ID {c.id} with patch: {patch}")
    try:
        for k, v in patch.model_dump(exclude_unset=True).items():
            setattr(c, k, v)
        db.add(c)
        db.commit()
        db.refresh(c)
        logger.debug(f"Contact updated successfully: {c}")
        return c
    except Exception as e:
        logger.exception(f"Failed to update contact ID {c.id}: {e}")
        db.rollback()
        raise


def delete_contact(db: Session, c: models.Contact):
    logger.debug(f"Deleting contact: {c}")
    try:
        db.delete(c)
        db.commit()
        logger.debug(f"Contact deleted successfully: ID {c.id}")
    except Exception as e:
        logger.exception(f"Failed to delete contact ID {c.id}: {e}")
        db.rollback()
        raise
