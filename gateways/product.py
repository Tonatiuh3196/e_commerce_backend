from sqlmodel import Session, select
from models.product import Product
from fastapi import Depends, HTTPException
from database import get_session

class ProductGateway:
    @classmethod
    def create_product(cls, product: Product, session: Session = Depends(get_session)) -> Product:
        # Verificar si el producto existe
        if product.id is not None:
            existing_product = session.exec(select(Product).where(Product.id == product.id)).first()
        if existing_product:
            raise HTTPException(status_code=400, detail="Product ID already exists")
    
        new_product = Product(**product.dict())
        session.add(new_product)
        session.commit()
        session.refresh(product)
        return product
    
    @classmethod
    def get_products(cls, session: Session = Depends(get_session)) -> list[Product]:
        return session.exec(select(Product)).all()
    
    @classmethod
    def get_product(cls, product_id: int, session:  Session = Depends(get_session)) -> Product:
        product =  session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    @classmethod
    def delete_product(cls, product_id: int, session: Session = Depends(get_session)) -> Product:
        product = cls.get_product(product_id, session) # Llamamos al metodo get_product para validar
        session.delete(product)
        session.commit()
        return product
        
    @classmethod
    def update_product(cls, product_id: int, product_data: Product, session: Session = Depends(get_session)) -> Product:
        product = cls.get_product(product_id, session)

        # Validar que el ID coincida
        if product_id != product_data.id:
            raise HTTPException(status_code=404, detail="Product ID does not macht")
        
        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @classmethod
    def patch_product(cls, product_id: int, data: dict, session: Session = Depends(get_session)) -> Product:
        product = cls.get_product(product_id, session)

        for key, value in data.items():
            if key in product.dict(): #Solo se actualiza si la clave existe en el modelo
                setattr(product, key, value)
            
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
