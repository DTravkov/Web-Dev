from core.config import settings
from core.logging import get_logger
logger = get_logger(__name__)


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.model import Base



DATABASE_URL = settings.DATABASE_URL
#async session asigned with factory pattern. basic alchemy practice
engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False, autoflush=True)

#creates tables if not exists. app runs it everytime when loaded (check /app/core/ls.py)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Database has been set up")

#yields database for Depends, and manages its lifespan
async def get_db():
    async with new_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
