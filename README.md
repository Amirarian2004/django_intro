# Hello Django — Multipage Site

A multipage Django project built across Weeks 7 and 8 of the Backend
Development Roadmap. It started as a static multipage site (URL routing,
function-based views, template inheritance) and now includes a real
PostgreSQL-backed blog app with models, migrations, an admin panel, and
ORM-driven views.

## Features

### Week 7 — Static multipage site (core app)

- Home page — welcome message with optional `?name=...` query parameter
- About page — greeting, also supports `?name=...`
- Projects page — renders a list of projects with status icons
- Post detail page — dynamic URL routing with `<int:post_id>`
- Shared navigation via template inheritance (`base.html`)
- Static CSS styling

### Week 8 — Blog app (database-backed)

- `Post` model with validated fields (`title`, `content`, `summary`,
  `status`, `is_featured`, `view_count`, `created_at`, `updated_at`)
- `choices` on `status` (draft / published) with dropdown in admin
- Django admin panel with a customized `PostAdmin`
  (`list_display`, `search_fields`, `list_filter`, `ordering`)
- Two ORM-driven views:
  - `/blog/` — all posts, newest first
  - `/blog/published/` — only published posts
- Templates loop over real QuerySets — no hardcoded data
- PostgreSQL as the database (via `psycopg2-binary`)
- Secrets kept out of source control with `python-dotenv` and `.env`

## Tech Stack

- Python 3.13
- Django 6.1
- PostgreSQL
- `psycopg2-binary` (PostgreSQL driver)
- `python-dotenv` (environment variable loading)
- Ruff (linter)

## Setup

### 1. Clone and enter the project

```
git clone <repo-url>
cd django_intro
```

### 2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```
pip install django==6.1 psycopg2-binary python-dotenv
```

### 4. Create the PostgreSQL database

```
psql -U postgres
CREATE DATABASE django_intro_db;
\q
```

### 5. Create the `.env` file (project root, next to `manage.py`)

```
DB_NAME=django_intro_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

> `.env` is listed in `.gitignore` and must never be committed.

### 6. Apply migrations

```
python manage.py migrate
```

### 7. Create an admin superuser (optional)

```
python manage.py createsuperuser
```

### 8. Run the development server

```
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Routes

| URL | Description |
| --- | --- |
| `/` | Home page — `?name=YourName` changes the greeting |
| `/about/` | About page — also supports `?name=...` |
| `/projects/` | Projects list with status icons |
| `/post/<int:post_id>/` | Post detail page (static) |
| `/blog/` | Blog list — all posts from the database, newest first |
| `/blog/published/` | Blog list — only published posts |
| `/admin/` | Django admin panel |

## Project Structure

```
django_intro/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   └── post_detail.html
│   ├── static/core/
│   │   └── style.css
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_post_is_featured_post_status_post_summary_and_more.py
│   │   └── 0003_post_view_count.py
│   ├── templates/blog/
│   │   └── post_list.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── venv/                # local only — not committed
├── .env                 # local only — not committed
├── .gitignore
├── manage.py
└── README.md
```

## Notes

- `venv/` and `.env` are intentionally not committed to Git. Each
  environment creates its own.
- `db.sqlite3` is a leftover from Week 7 — the project now uses
  PostgreSQL.
- Migrations are the source of truth for the schema. Run `migrate`
  after pulling changes.

## Author

Arian — Backend Development Roadmap, Phase 2