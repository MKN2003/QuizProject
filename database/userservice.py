from database.models import User, UserAnswers, Questions, Result
from datetime import datetime
from database import get_db


def get_all_users_db():
    db = next(get_db())

    users = db.query(User).all()
    return users

