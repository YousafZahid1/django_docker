# Django Blog Project

A simple blog application built with Django that allows authenticated users to create blog posts while allowing anyone to read them.

## Features
- User authentication with Ion OAuth
- Create, read blog posts
- Admin interface for post management
- SQLite database

## Setup Instructions

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

## Project Structure
- `blog/` - Main application directory
  - `templates/` - HTML templates
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL routing
  - `auth.py` - Custom authentication
- `blog_project/` - Project settings
- `requirements.txt` - Project dependencies 