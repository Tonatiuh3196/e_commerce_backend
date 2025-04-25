from sqlmodel import create_engine, SQLModel

from core.base import DB_PORT, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=False)

#SQLModel.metadata.create_all(engine)