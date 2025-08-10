from fastapi import Depends
from crud.restaurant_repo_sqlalchemy import RestaurantRepoSQLAlchemy
from services.restaurant_service import RestaurantService
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession



async def get_restaurant_service(db: AsyncSession = Depends(get_db)) -> RestaurantService:
    repo = RestaurantRepoSQLAlchemy(db)
    return RestaurantService(repo)