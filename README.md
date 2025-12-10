# Установка и запуск
1. Клонировать проект
```
git clone https://github.com/herbaa/practic23.git
cd news-blog
```
2. Установить зависимости
```
uv sync
```
3. Создать .env файл в корне:
```
SECRET_KEY="your-key"
DEBUG=True
```
Вместо your-key вставить значение SECRET_KEY из файла settings.py

4. Применить миграции
```
uv run manage.py migrate
```
5. Создать суперпользователя
```
uv run manage.py createsuperuser
```
6. Запуск сервера
```
uv run manage.py runserver
```
