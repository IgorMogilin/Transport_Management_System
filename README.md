# TMS (Transport Management System)

Система управления транспортом и перевозками. Проект представляет собой бэкенд-часть TMS с моделями данных на SQLAlchemy, миграциями Alembic и строгой типизацией.

## 🚀 Технологии

- Python 3.11+
- SQLAlchemy 2.0 (новый синтаксис `Mapped`/`mapped_column`)
- Alembic (миграции)
- PostgreSQL 16
- Docker / Docker Compose
- Ruff (линтер + форматер)
- Pre-commit hooks
- MyPy (проверка типов)

## 📦 Развертывание проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/IgorMogilin/Transport_Management_System.git
cd Transport_Management_System
```

### 2.  Создание виртуального окружения
```bash
uv venv
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows
```

### 3. Установка зависимостей
```bash
uv pip install -e .
```

### 4. Настройка pre-commit hooks
```bash
pre-commit install
pre-commit run --all-files  # проверить что всё работает
```

### 5. Настройка окружения
```bash
cp .env.example .env
# Отредактируйте .env под свои параметры (по умолчанию уже настроено)
```

### 6. Запуск PostgreSQL через Docker
```bash
docker-compose up -d
# Проверка: docker ps
```

### 7. Применение миграций
```bash
alembic upgrade head
```

### 8. Проверка базы данных
```bash
docker exec -it tms_postgres psql -U postgres -d tms_db -c "\dt"
# Должны увидеть таблицы: user, vehicle, location, order
```

## Автор
Igor Mogilin
GitHub: [IgorMogilin](https://github.com/IgorMogilin)
