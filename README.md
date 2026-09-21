# Telegram Task Manager

Асинхронный Telegram-бот и REST API для управления задачами. Проект показывает работу с Telegram Bot API, FastAPI, PostgreSQL, async SQLAlchemy и миграциями базы данных.

## Демо

После локального запуска API доступна интерактивная документация Swagger UI:

- `http://127.0.0.1:8000/docs` — проверка всех API-методов в браузере;
- команда `/start` в Telegram — приветствие пользователя ботом.

## Возможности

- запуск Telegram-бота в асинхронном режиме через Aiogram;
- создание и получение пользователей по Telegram ID;
- создание, просмотр и удаление задач;
- изменение статуса выполнения задачи;
- хранение пользователей и задач в PostgreSQL;
- асинхронная работа с базой данных;
- управление схемой базы данных через Alembic;
- автоматически сгенерированная документация OpenAPI/Swagger.

## Технологии

- Python
- Aiogram 3
- FastAPI
- PostgreSQL
- SQLAlchemy (async) + asyncpg
- Alembic
- Pydantic

## Быстрый запуск

### 1. Подготовьте проект

```bash
git clone https://github.com/aiaz-shakirov/telegram-task-manager.git
cd telegram-task-manager

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Для Windows активация окружения выполняется командой:

```powershell
.venv\Scripts\activate
```

### 2. Настройте переменные окружения

```bash
cp .env.example .env
```

Заполните `.env` своими значениями:

```dotenv
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/telegram_task_manager
```

Настоящий токен бота и пароль базы данных не должны попадать в Git.

### 3. Подготовьте базу данных

Создайте базу PostgreSQL с именем `telegram_task_manager`, затем примените миграции:

```bash
alembic upgrade head
```

### 4. Запустите API

```bash
uvicorn app.main:app --reload
```

API будет доступно по адресу `http://127.0.0.1:8000`, документация — по адресу `http://127.0.0.1:8000/docs`.

### 5. Запустите Telegram-бота

В отдельном терминале с активированным виртуальным окружением:

```bash
python main.py
```

## API

| Метод | Маршрут | Назначение |
| --- | --- | --- |
| `POST` | `/users/` | Создать пользователя |
| `GET` | `/users/{telegram_id}` | Получить пользователя по Telegram ID |
| `GET` | `/tasks/` | Получить список задач |
| `GET` | `/tasks/{task_id}` | Получить задачу |
| `POST` | `/tasks/` | Создать задачу |
| `PATCH` | `/tasks/{task_id}` | Изменить статус задачи |
| `DELETE` | `/tasks/{task_id}` | Удалить задачу |

## Структура проекта

```text
.
├── app/
│   ├── routers/        # API-маршруты пользователей и задач
│   ├── database.py     # Асинхронное подключение к PostgreSQL
│   ├── main.py         # FastAPI-приложение
│   ├── models.py       # SQLAlchemy-модели
│   └── schemas.py      # Pydantic-схемы
├── migrations/         # Миграции Alembic
├── .env.example        # Пример переменных окружения без секретов
├── alembic.ini         # Конфигурация Alembic
├── main.py             # Точка запуска Telegram-бота
└── requirements.txt    # Python-зависимости
```

## Статус проекта

Это MVP: Telegram-бот уже запускается и отвечает на `/start`, а управление задачами реализовано через REST API. Следующий этап — связать команды бота с API задач и добавить наглядное GIF-демо.
