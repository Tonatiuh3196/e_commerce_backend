from fastapi import APIRouter, Depends
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from gateways.product import ProductGateway
from sqlmodel import Session
from database import get_session 

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    return ProductGateway.create_product(product, session)

@router.get("/", response_model=list[ProductResponse])
def get_products(session: Session = Depends(get_session)):
    return ProductGateway.get_products(session)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, session: Session = Depends(get_session)):
    return ProductGateway.get_product(product_id, session)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, session: Session = Depends(get_session)):
    return ProductGateway.update_product(product_id, product, session)

@router.patch("/{product_id}", response_model=ProductResponse)
def patch_product( product_id: int, data: dict, session: Session = Depends(get_session)):
    return ProductGateway.patch_product(product_id, data, session)

@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    return ProductGateway.delete_product(product_id, session)



