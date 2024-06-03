from fastapi import FastAPI

from api.test_api.tests import test_router
from database import Base, engine
from database.userservice import get_all_users_db
from api.user_api.users import user_router

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(test_router)
