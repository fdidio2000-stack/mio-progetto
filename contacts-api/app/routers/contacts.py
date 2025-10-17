import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..db import get_db, Base, engine
from .. import crud, schemas, models
from ..services.enrich import gravatar_url, check_avatar_exists
from sqlalchemy import text
import json

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contacts", tags=["contacts"])



logger.info("Creating all tables on startup (if not exist)")
   


@router.post("", response_model=schemas.ContactOut, status_code=201)
async def create(data: schemas.ContactCreate, db: Session = Depends(get_db)):
    logger.info(f"Attempting to create contact: {data.full_name} ({data.email})")
    
    if crud.get_by_email(db, str(data.email)):
        logger.info(f"Contact creation failed: email already exists ({data.email})")
        raise HTTPException(409, "Email already exists")
    
    c = crud.create_contact(db, data)
    logger.debug(f"Contact created: {c}")

    avatar = gravatar_url(c.email)
    logger.debug(f"Generated gravatar URL: {avatar}")
    
    if await check_avatar_exists(avatar):
        logger.debug("Gravatar exists, updating avatar_url")
        c = crud.update_contact(db, c, schemas.ContactUpdate(avatar_url=avatar))
    
    logger.info(f"Contact created successfully with ID: {c.id}")
    return c


@router.get("/{cid}", response_model=schemas.ContactOut)
def get_one(cid: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching contact with ID: {cid}")
    
    c = crud.get_contact(db, cid)
    if not c:
        logger.info(f"Contact not found: ID {cid}")
        raise HTTPException(404)
    
    logger.debug(f"Contact found: {c}")
    return c


@router.put("/{cid}", response_model=schemas.ContactOut)
async def update(cid: int, patch: schemas.ContactUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating contact ID {cid}")
    logger.debug(f"Update data received: {patch}")
    
    c = crud.get_contact(db, cid)
    if not c:
        logger.info(f"Contact to update not found: ID {cid}")
        raise HTTPException(404)
    
    email_changed = patch.email and patch.email != c.email
    c = crud.update_contact(db, c, patch)
    logger.debug(f"Contact updated with new data: {c}")
    
    if email_changed:
        avatar = gravatar_url(c.email)
        logger.debug(f"Email changed, checking new gravatar: {avatar}")
        if await check_avatar_exists(avatar):
            logger.debug("New gravatar exists, updating avatar_url")
            c = crud.update_contact(db, c, schemas.ContactUpdate(avatar_url=avatar))
    
    logger.info(f"Contact updated successfully: ID {c.id}")
    return c


@router.delete("/{cid}", status_code=204)
def delete(cid: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting contact ID: {cid}")
    
    c = crud.get_contact(db, cid)
    if not c:
        logger.info(f"Contact to delete not found: ID {cid}")
        raise HTTPException(404)
    
    crud.delete_contact(db, c)
    logger.info(f"Contact deleted successfully: ID {cid}")
    return


@router.get("", response_model=list[schemas.ContactOut])
def list_contacts(
    query: str = "", tag: str | None = None, limit: int = Query(50, le=200), offset: int = 0,
    db: Session = Depends(get_db),
):
    logger.info(f"Listing contacts (query='{query}', tag='{tag}', limit={limit}, offset={offset})")
    
    q = db.query(models.Contact)
    
    if query:
        like = f"%{query.lower()}%"
        q = q.filter((models.Contact.full_name.ilike(like)) | (models.Contact.email.ilike(like)))
        logger.debug(f"Applied search filter: {like}")
    
    if tag:
        q = q.filter(models.Contact.tags.like(f'%"{tag}"%'))
        logger.info(f"Applied tag filter: {tag}")
    
    results = q.offset(offset).limit(limit).all()
    logger.info(f"Found {len(results)} contacts")
    logger.debug(f"Results: {results}")
    return results
