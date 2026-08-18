# Use official python image
FROM python:3.11-slim

# Set environment  variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose Django's standard production port
EXPOSE 8000

# Run migrations, collect static files, and start Gunicorn server

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    exec gunicorn myproject.wsgi:application --bind 0.0.0:8000 --workers 3