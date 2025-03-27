from sqlmodel import Session, select
from models.user import User
from database import get_session
from fastapi import Depends, HTTPException


class UserGateway:
    @classmethod
    def create_user(cls, user: User, session: Session = Depends(get_session)) -> User:
        # verificamos si ya existe en la base de datos.
        if user.id is not None:
            existing_user = session.exec(select(User).where(User.id == user.id)).first()
            if existing_user:
                raise HTTPException(status_code=400, detail="User ID already exists.")

    # Creamos un nuevo usuario con el `id` proporcionado o dejamos que la base de datos lo genere
        new_user = User(**user.dict())  
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user  # Ahora devolverá el `id` generado o el que se envió

    @classmethod
    def get_users(cls, session: Session = Depends(get_session)) -> list[User]:
        return session.exec(select(User)).all()

    @classmethod
    def get_user(cls, user_id: int, session: Session = Depends(get_session)) -> User:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return user

    @classmethod
    def delete_user(cls, user_id: int, session: Session = Depends(get_session)) -> User:
        user = cls.get_user(user_id, session)  # Llamamos al método get_user para validar
        session.delete(user)
        session.commit()
        return user

    @classmethod
    def update_user(cls, user_id: int, user_data: User, session: Session = Depends(get_session)) -> User:
        user = cls.get_user(user_id, session)
        
        # Validamos que el ID coincida
        if user_id != user_data.id:
            raise HTTPException(status_code=400, detail="User ID does not match.")

        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @classmethod
    def patch_user(cls, user_id: int, data: dict, session: Session = Depends(get_session)) -> User:
        user = cls.get_user(user_id, session)

        for key, value in data.items():
            if key in user.dict():  # Solo actualizar si la clave existe en el modelo
                setattr(user, key, value)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user