# Hello Django — Multipage Site

A multipage Django project built during Week 7 of the Backend Development Roadmap.
This project demonstrates URL routing, function-based views, template inheritance,
static file handling, and dynamic content rendering.

## Features

- Home page — shows a welcome message with optional `?name=...` query parameter
- About page — displays a greeting, also supports `?name=...`
- Projects page — renders a list of projects with status icons (✅ Done / ⏳ In progress)
- Post detail page — demonstrates dynamic URL routing with `<int:post_id>`
- Shared navigation using template inheritance (`base.html`)
- Static CSS styling

## Tech Stack

- Python 3.13
- Django 6.1
- SQLite (default database)

## How to Run

1. Clone or download the project and navigate to the project folder:
   `cd django_intro`

2. Create a virtual environment:
   `python -m venv venv`

3. Activate the virtual environment:
   `venv\Scripts\Activate.ps1`

4. Install Django:
   `pip install django==6.1`

5. Start the development server:
   `python manage.py runserver`

6. Open your browser and go to:
   `http://127.0.0.1:8000/`

> **Note:** The `venv/` directory is intentionally not committed to Git.
> Each user should create their own virtual environment.

## Routes

| **URL**                | **Description**                                    |
| ---------------------- | -------------------------------------------------- |
| `/`                    | Home page — `?name=YourName` changes the greeting |
| `/about/`              | About page — also supports `?name=...`            |
| `/projects/`           | Projects list with status icons                   |
| `/post/<int:post_id>/` | Post detail page                                  |

## Project Structure

django_intro/
├── config/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── projects.html
│   │       └── post_detail.html
│   ├── static/
│   │   └── core/
│   │       └── style.css
│   ├── __init__.py
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── venv/                # Created locally; not committed to Git
├── db.sqlite3
├── manage.py
└── README.md

## Author

Arian — Backend Development Roadmap, Phase 2