from sqlmodel import Session, select
from models.product import Product
from schemas.product import ProductCreate, productUpdate
from pydantic import TypeAdapter
from fastapi import HTTPException 

adapter_create = TypeAdapter(ProductCreate)
adapter_update = TypeAdapter(productUpdate)

def create_product(session: Session, product_create: ProductCreate):
    product_data = adapter_create.validate_python(product_create)
    product = Product(**product_data.model_dum())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_product(session: Session, product_id: int):
    return session.exec(select(Product).where(Product.id == product_id)).first()

def delete_product(session: Session, product_id: int):
    product = get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    session.delete(product)
    session.commit()

def update_product(session: Session, product_id: int, product_update: ProductCreate):
    product = get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    product_data = adapter_create.validate_python(product_update).model_dump()
    for key, value in product_data.items():
        setattr(product, key, value)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def patch_product(session: Session, product_id, product_patch: productUpdate):
    product = get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product_data =  adapter_update.validate_python(product_patch).model_dump()
    for key, value in product_data.items():
        setattr(product, key, value)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
