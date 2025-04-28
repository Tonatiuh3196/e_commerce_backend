from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.v1 import products
from api.v1 import users

from db.session import init_db
from api.v1 import cartShoppings

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1/users", tags=["User"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Product"])
app.include_router(cartShoppings.router, prefix="/api/v1/cartShoppings", tags=["CartShopping"])

