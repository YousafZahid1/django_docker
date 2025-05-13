# Django Blog Project with Docker and Celery

A simple blog application built with Django that allows authenticated users to create blog posts while allowing anyone to read them. The application uses Docker for containerization and Celery for background tasks.

## Features
- User authentication with Ion OAuth
- Create, read blog posts
- Admin interface for post management
- SQLite database
- Celery background tasks
- Docker containerization
- Redis for message broker

## Setup Instructions

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/YousafZahid1/Django.git
cd Django
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

4. Run migrations:
```bash
python3 manage.py migrate
```

5. Create a superuser:
```bash
python3 manage.py createsuperuser
```

6. Run the development server:
```bash
python3 manage.py runserver
```

7. Visit http://127.0.0.1:8000/ to see the blog

### Docker Setup

1. Build and start the containers:
```bash
docker-compose up --build
```

2. In a new terminal, run migrations:
```bash
docker-compose exec web python3 manage.py migrate
```

3. Create a superuser:
```bash
docker-compose exec web python3 manage.py createsuperuser
```

4. Visit http://localhost:8000/ to see the blog

## Project Structure
- `blog/` - Main application directory
  - `templates/` - HTML templates
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL routing
  - `auth.py` - Custom authentication
  - `tasks.py` - Celery tasks
- `blog_project/` - Project settings
  - `celery.py` - Celery configuration
- `requirements.txt` - Project dependencies
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker services configuration

## Docker Services
- `web` - Django application
- `celery` - Celery worker
- `celerybeat` - Celery beat scheduler
- `redis` - Message broker

## Celery Tasks
- Updates the `last_updated_date` field of all blog posts every 5 minutes 