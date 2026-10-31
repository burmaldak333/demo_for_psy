#!/usr/bin/env bash
# Устанавливаем зависимости
pip install -r requirements.txt
# Собираем статику (CSS)
python manage.py collectstatic --no-input
# Применяем миграции (на случай если добавишь БД)
python manage.py migrate