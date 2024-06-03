from fastapi import APIRouter
from database.testservice import get_question_db, get_10_leaders_db, add_question_db

test_router = APIRouter(prefix='/test', tags=['API for test'])


@test_router.get('/all-questions')
async def all_questions():
    return get_question_db()


@test_router.get('/top-10-leaders')
async def get_leaders():
    return get_10_leaders_db()


@test_router.post('/add-questions')
async def add_questions(main_questions: str, v1: str, v2: str, v3: str, v4: str, correct_answer: int ):
    question = add_question_db(main_questions, v1, v2, v3, v4, correct_answer)
    return question

