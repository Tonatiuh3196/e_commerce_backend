from sqlmodel import Session, select
from models.cardShopping import CardShopping
from schemas.cardShopping import CardShoppingCreate
from fastapi import HTTPException
from uuid import UUID

def create_cardShopping(session: Session, cardShopping_data: CardShoppingCreate):
    cardShopping = CardShopping(
        user_id=cardShopping_data.user_id,
        products=[item.model_dump() for item in cardShopping_data.productos]
    )
    session.add(cardShopping)
    session.commit()
    session.refresh(cardShopping)
    return cardShopping

def get_cardShopping(session: Session, cardShopping_id: UUID):
    cardShopping = session.exec(select(CardShopping).where(CardShopping.id == cardShopping_id)).first()
    if not cardShopping:
        raise HTTPException(status_code=404, detail="CardShopping not found")
    return cardShopping

def delete_cardShopping(session: Session, cardShopping_id: UUID):
    cardShopping = get_cardShopping(session, cardShopping_id)
    session.delete(cardShopping)
    session.commit()

def update_cardShopping(session: Session, cardShopping_id: UUID, cardShopping_data: CardShoppingCreate):
    cardShopping= get_cardShopping(session, cardShopping_id)
    cardShopping.user_id = cardShopping_data.user_id
    cardShopping.products = [item.model_dump() for item in cardShopping_data.productos]
    session.add(cardShopping)
    session.commit()
    session.refresh(cardShopping)
    return cardShopping

