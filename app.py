from fastapi import FastAPI
from routes import user, product, shoppingCart
from database import create_db_and_tables

app = FastAPI()
create_db_and_tables()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(shoppingCart.router, prefix="/shoppingCart", tags=["ShoppingCart"])