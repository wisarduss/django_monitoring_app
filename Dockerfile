FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# Запускаем Gunicorn с переменной окружения для метрик
CMD ["sh", "-c", "GUNICORN_METRICS=1 gunicorn --bind 0.0.0.0:8000 --workers 4 --preload app.wsgi:application"]