# IT-проект "Образовательная платформа ООП"

## Ссылки:

### Архитектура проекта:

> [Miro]()

### Цели и задачи:

> [Trello](https://trello.com/b/Oj3UHJCU/gigoop) (закрытый доступ)

### Структура базы данных:

> [Figma](https://www.figma.com/board/GPE3nndbkOOPY9NNyKKXWF/gigaOOP-schema?node-id=0-1&t=QtS3mkE6LDU6i4ud-1)

## Запуск проекта
### Запуска сервера backend
Запуск проекта осуществляется после того, как вы клонировали репозиторий себе на локальную машину.

Создайте файл переменных среды .env:
| Variable | Value example |
| ------------- | ------------- |
| DB_NAME | gigaoop |
| DB_NAME_TEST | gigaoop_test |
| SECRET_AUTH | 1234 |

Для запуска backend используется сервер uvicorn.
Установите виртуальную среду python - venv в корень проекта:
```
python -m venv .venv
```
Затем войдите в venv с помощью команды (Windows):
```
source .venv/Scripts/activate
```
Перейдите в папку бэкенда:
```
cd backend
```
Выполните установку зависимостей:
```
pip install -r requirements.txt
```
Примените миграции:
```
alembic upgrade head
```
Запустите сервер uvicorn:
```
uvicorn main:app
```
### Запуск сервера frontend
Из корня проекта перейдите в папку фронтенда:
```
cd frontend
```
Установите зависимости для фронтенда:
```
npm install
```
Запустите сервер фронтенда:
```
npm run dev
```
