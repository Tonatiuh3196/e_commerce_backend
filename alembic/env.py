from __future__ import with_statement
import sys
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar las clases de los modelos
from db.session import engine
from core.config import settings  # <-- Asegúrate de importar la configuración

# Importar modelos
from models.product import Product
from models.user import User
from models.cartShopping import CartShopping

# Configuración de Alembic
config = context.config
fileConfig(config.config_file_name)

# MetaData de SQLModel
target_metadata = SQLModel.metadata

# Configurar la URL de la base de datos desde settings.py
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

def run_migrations_offline() -> None:
    """Modo offline para ejecutar migraciones."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Modo online para ejecutar migraciones."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
