from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create default superuser if not exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "Admin"
        password = "admin123"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="admin@example.com",
                password=password
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write("Superuser already exists")
