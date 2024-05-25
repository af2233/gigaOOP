from sqlalchemy import Column, String, Integer, ForeignKey

from ...db.session import Base


class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
