from sqlalchemy import Column, String, Integer, ForeignKey

from ...db.session import Base


class UserAnswer(Base):
    __tablename__ = 'user_answers'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
    correct = Column(Integer, default=0)
