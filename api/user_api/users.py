from fastapi import APIRouter
from database.userservice import get_all_users_db, user_answer_db, register_user_db, plus_point_db

user_router = APIRouter(prefix='/user', tags=['API for users'])


@user_router.get('/all-users')
async def all_users():
    return get_all_users_db()


@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    reg = register_user_db(name, phone_number, level)
    return reg


@user_router.get('/leaders')
async def get_leaders(user_id: int, id: int, level: str, correct_answer: int):
    leaders = user_answer_db(user_id, id, level, correct_answer)
    return f'Лидеры: {leaders}'


@user_router.post('/done')
async def done(user_id: int, correct_answers: int, level: str):
    result = plus_point_db(user_id, correct_answers, level)
    return f'Результат: {result}'
