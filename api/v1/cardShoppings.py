from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from db.session import get_session
from sqlmodel import Session
from schemas.cardShopping import CardShoppingCreate
from models.cardShopping import CardShopping
from crud.cardShopping import create_cardShopping, get_cardShopping, delete_cardShopping, update_cardShopping

router = APIRouter()

@router.post("/cardShopping", response_model=CardShopping)
def create(cardShopping_data: CardShoppingCreate, session: Session = Depends(get_session)):
    return create_cardShopping(session, cardShopping_data)

@router.get("/cardShopping/{cardShopping_id}", response_model=CardShopping)
def read(cardShopping_id: UUID, session: Session = Depends(get_session)):
    return get_cardShopping(session, cardShopping_id)

@router.delete("/cardShopping/{cardShopping_id}", status_code=204)
def delete(cardShopping_id: UUID, session: Session = Depends(get_session)):
    delete_cardShopping(session, cardShopping_id)

@router.put("/cardShopping/{cardShopping_id}", response_model=CardShopping)
def update(cardShopping_id: UUID, cardShopping_data: CardShoppingCreate, session: Session = Depends(get_session)):
    return update_cardShopping(session, cardShopping_id, cardShopping_data)
