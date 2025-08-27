from fastapi import FastAPI
from routes import router
import database

app=FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    print("Conectando...")
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)