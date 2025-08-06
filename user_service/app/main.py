import uvicorn


from fastapi import FastAPI, Depends
from dotenv import load_dotenv

load_dotenv() 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from middleware.logging import LoggingMiddleware
from routes.user_router import router as user_router
from database import get_db
 # Load environment variables from .env file

app = FastAPI(title="User Service")


app.add_middleware(LoggingMiddleware)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"msg": "User Service is running"}

@app.get("/db-health")
async def db_health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
    
