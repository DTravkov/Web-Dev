from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database import setup_database, engine

 
# fastapi's lifespans give us ability to run some code before app starts up, and after it finishes working.
# this particularly ensures db is set up (tables are intact), adn closes singleton http client along with db engine on exit
# therefore - smooth startup and graceful exit for an app
@asynccontextmanager
async def lifespan(app: FastAPI):

    await setup_database()
    
    yield

    await engine.dispose()
    
