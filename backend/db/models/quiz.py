from sqlalchemy import Column, Integer, ForeignKey, String

from db.session import Base

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)

class QuizQuestion(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
    answer = Column(String)

