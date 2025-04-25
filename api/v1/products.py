from fastapi import APIRouter, Depends, HTTPException

from schemas.product import ProductCreate, ProductRead, productUpdate
from crud.product import create_product, get_product, delete_product, update_product, patch_product 
from db.session import get_session

router = APIRouter()

@router.post("/product", response_model=ProductRead)
def create(product: ProductCreate, session=Depends(get_session)):
    return create_product(session, product)

@router.get("/product/{product_id}", response_model=ProductRead)
def read(product_id: int, session = Depends(get_session)):
    product = get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product

@router.delete("/product/{product_id}", status_code=204)
def delete(product_id: int, session = Depends(get_session)):
    delete_product(session, product_id)

@router.put("/product/{product_id}", response_model=ProductRead)
def update(product_id: int, product_update: productUpdate, session = Depends(get_session)):
    return update_product(session, product_id, product_update)

@router.patch("/product/{product_id}", response_model=ProductRead)
def patch(product_id: int, product_patch: ProductCreate, session=Depends(get_session)):
    return patch_product(session, product_id, product_patch)
