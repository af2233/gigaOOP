from sqlalchemy import Column, String, ForeignKey, Integer

from db.session import Base


class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
