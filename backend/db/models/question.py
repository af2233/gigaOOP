from sqlalchemy import Column, String, Integer, ForeignKey

from db.session import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
    questions_text = Column(String)
