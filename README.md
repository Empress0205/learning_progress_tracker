# Learning Progress Tracker API

A REST API that helps learners organise subjects, set goals, log progress and schedule reminders. Built with Django REST Framework.

## Endpoints

| Path | Description |
| --- | --- |
| `/register/`, `/login/`, `/logout/` | Authentication |
| `/subjects/`, `/subjects/<id>/` | Subjects being studied |
| `/goals/`, `/goals/<id>/` | Learning goals (can be marked complete) |
| `/progress/`, `/progress/<id>/` | Progress entries |
| `/reminders/`, `/reminders/<id>/` | Study reminders |

## Stack

Python · Django 5.2 · Django REST Framework · SQLite

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key — set a long random value outside local development | development-only key |
| `DJANGO_DEBUG` | `True` or `False` | `True` |
