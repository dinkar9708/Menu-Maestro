from fastapi import FastAPI, Depends
from dotenv import load_dotenv
load_dotenv() 

import uvicorn
from database import init_db
from routes import restaurant_router


app = FastAPI(title="Menu Maestro Restaurant Service")

@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(restaurant_router.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
