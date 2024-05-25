from sqlalchemy import Column, String, Integer, ForeignKey

from db.session import Base

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    answer_text = Column(String)
    proper = Column(Integer, default=0)
