from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserCreate
from crud.user_repository import UserRepository

class UserService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register_user(self, user: UserCreate):
        existing_user = await self.repo.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return await self.repo.create(user)
