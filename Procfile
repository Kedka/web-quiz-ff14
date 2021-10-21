web: gunicorn myproject.wsgi
release: python manage.py collectstatic
release: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate