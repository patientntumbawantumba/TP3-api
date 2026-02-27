from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, SessionLocal
import os

PORT = int(os.environ.get("PORT", 8000))
#uvicorn.run(app, host="0.0.0.0", port=PORT)


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TP3 API")

# Dependency pour connexion DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all ads
@app.get("/ads", response_model=List[schemas.AdResponse])
def get_ads(db: Session = Depends(get_db)):
    return db.query(models.Ad).all()

# GET one ad
@app.get("/ads/{ad_id}", response_model=schemas.AdResponse)
def get_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if not ad:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad

# POST create ad
@app.post("/ads", response_model=schemas.AdResponse)
def create_ad(ad: schemas.AdCreate, db: Session = Depends(get_db)):
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

# DELETE ad
@app.delete("/ads/{ad_id}")
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if not ad:
        raise HTTPException(status_code=404, detail="Ad not found")
    db.delete(ad)
    db.commit()
    return {"message": "Ad deleted successfully"}