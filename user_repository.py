from sqlalchemy.ext.asyncio import AsyncSession

from api_models import UserCreate
from models import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_create: UserCreate):
        user = User(
            name=user_create.name,
            email=user_create.email
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    