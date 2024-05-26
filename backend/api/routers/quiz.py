from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload


from api.deps import get_db

from db.models.quiz import Quiz, QuizQuestion
from db.schemas.quiz import QuizCreate, QuizRead, QuizUpdate

router = APIRouter()

@router.post("/", response_model=QuizRead, status_code=status.HTTP_201_CREATED)
async def create_quiz(quiz: QuizCreate, db: AsyncSession = Depends(get_db)):
    new_quiz = Quiz(**quiz.dict(exclude={"questions"}))
    async with db as session:
        session.add(new_quiz)
        await session.commit()
        await session.refresh(new_quiz)

        for question in quiz.questions:
            new_question = QuizQuestion(**question.dict(), quiz_id=new_quiz.id)
            session.add(new_question)
        
        await session.commit()
        await session.refresh(new_quiz)

    return new_quiz

@router.get("/{quiz_id}", response_model=QuizRead)
async def read_quiz(quiz_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Quiz).where(Quiz.id == quiz_id).options(selectinload(Quiz.questions)))
        quiz = result.scalars().first()
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.get("/", response_model=list[QuizRead])
async def get_quizzes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Quiz).offset(skip).limit(limit))
        quizzes = result.scalars().all()
    return quizzes

@router.put("/{quiz_id}", response_model=QuizRead)
async def update_quiz(quiz_id: int, quiz_update: QuizUpdate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Quiz).where(Quiz.id == quiz_id).options(selectinload(Quiz.questions)))
        quiz = result.scalars().first()
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")

        update_data = quiz_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            if key == "questions":
                for question in quiz.questions:
                    session.delete(question)
                await session.commit()

                for question_data in value:
                    new_question = QuizQuestion(**question_data, quiz_id=quiz.id)
                    session.add(new_question)
            else:
                setattr(quiz, key, value)

        session.add(quiz)
        await session.commit()
        await session.refresh(quiz)
    return quiz

@router.delete("/{quiz_id}", response_model=None)
async def delete_quiz(quiz_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz = result.scalars().first()
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")

        await session.delete(quiz)
        await session.commit()
    return None






