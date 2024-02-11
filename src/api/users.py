from typing import Annotated

from services.users import UsersService
from api.dependencies import users_service

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
from models.users import User
from schemas.users import UserSchemaAdd


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


# @router.get('/get_users')
# async def get_users(session: AsyncSession = Depends(get_async_session)):
#     queryset = select(User)
#     result = await session.execute(queryset)
#     return {"users": result.mappings().all()}
#
#
# @router.post('/create_user')
# async def create_user(new_user: UserSchemaAdd ,session: AsyncSession = Depends(get_async_session)):
#     try:
#         statement = insert(User).values(**new_user.dict())
#         await session.execute(statement)
#         await session.commit()
#         return {'status': 'ok', 'user': new_user}
#     except Exception:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
#             'status': 'error'
#         })

@router.get('/get_users')
async def get_users(users_repo: Annotated[UsersService, Depends(users_service)]):
    result = await users_repo.get_users()
    return result


@router.post('/created_user')
async def created_user(user: UserSchemaAdd, users_repo: Annotated[UsersService, Depends(users_service)]):
    user = await users_repo.add_user(user)
    return user
