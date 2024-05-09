from sqlalchemy import Column, Integer, String, ForeignKey, Float

from database import Base


# основные таблицы

class User(Base):  # таблица пользователей
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    login = Column(String, unique=True)
    status = Column(Integer, default=0)


class Course(Base):  # таблица курсов
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Theme(Base):  # таблица тем
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey(Course.id))
    order = Column(Integer)


class UserCourseProgress(Base):  # прогресс пользователя по курсам
    __tablename__ = 'user_courses_PROGRESS'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    course_id = Column(Integer, ForeignKey(Course.id))
    last_theme_index = Column(Integer)  # max(order) from themes where course_id == themes.course_id


class Relation(Base):  # таблица связей студентов и преподавателей
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    teacher_id = Column(Integer, ForeignKey(Course.id))  # user status == 1


# таблицы, относящиеся к разделу 'Задачи'

class Task(Base):  # таблица задач
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    theme_id = Column(Integer, ForeignKey(Theme.id))
    task_name = Column(String)
    description = Column(String)


class UserTaskAnswer(Base):  # ответы пользователя на задачу
    __tablename__ = 'user_tasks_Answers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    task_id = Column(Integer, ForeignKey(Task.id))
    code_text = Column(String)
    isCorrect = Column(Integer)


class UserTaskProgress(Base):  # прогресс по задачам внутри темы
    __tablename__ = 'user_tasks_PROGRESS'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    theme_id = Column(Integer, ForeignKey(Theme.id))
    progress = Column(Float)


# таблицы, относящиеся к разделу 'Опросы'

class Quiz(Base):  # таблица викторин
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    theme_id = Column(Integer, ForeignKey(Theme.id))


class Quiestion(Base):  # таблица вопросов
    __tablename__ = 'quiestions'

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey(Quiz.id))
    quiestion_text = Column(String)


class Answer(Base):  # таблица ответов
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey(Quiz.id))
    quiestion_text = Column(String)


class UserQuiestionAnswer(Base):  # ответы пользователя на вопрос
    __tablename__ = 'user_quiestions_Answers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    quiestion_id = Column(Integer, ForeignKey(Quiestion.id))
    quiz_id = Column(Integer, ForeignKey(Quiz.id))
    isCorrect = Column(Integer)


class UserQuizProgress(Base):  # прогресс пользователя по викторине
    __tablename__ = 'user_quizzes_PROGRESS'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    quiz_id = Column(Integer, ForeignKey(Theme.id))
    progress = Column(Float)
