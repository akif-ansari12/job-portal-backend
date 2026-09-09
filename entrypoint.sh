#!/bin/sh

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Creating/updating superuser..."

python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and email and password:
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "email": email,
            "is_staff": True,
            "is_superuser": True,
        }
    )

    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()

    print(f"Superuser {'created' if created else 'updated'} successfully.")
else:
    print("Superuser environment variables are not configured.")

PY

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000