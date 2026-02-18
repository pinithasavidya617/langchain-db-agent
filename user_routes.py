from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api_models import UserCreate, UserResponse
from database_config import get_db
from user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_create : UserCreate, db: AsyncSession = Depends(get_db)):

    user_repo = UserRepository(db)
    user = await user_repo.create(user_create)
    return user