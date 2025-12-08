import os
import django
from django.contrib.auth import get_user_model

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") # Agar folder name alag hai to change karein
django.setup()

User = get_user_model()

# Environment variables se details lo
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123') # Default password agar env nahi mila

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username, email, password)
else:
    print("Superuser already exists. Skipping creation.")