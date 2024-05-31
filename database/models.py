from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    level = Column(String, default='Select your level', nullable=False)
    datetime = Column(DateTime)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(Integer, nullable=False)
    timer = Column(DateTime)


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answers = Column(Integer, default=0)
    level = Column(String, nullable=False)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')


class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    q_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey('users.level'))
    user_answer = Column(String, nullable=False)
    correctness = Column(Boolean, default=False)
    timer = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    question_fk = relationship(Questions, foreign_keys=[q_id], lazy='subquery')
