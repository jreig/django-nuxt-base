from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate superusers, users and app data"

    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")

        print("Seeding database...")

        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            print("Creating default superuser")
            User.objects.create_superuser(
                username="Tyris", email=None, password="Tyris123"
            )
            print("Super user Tyris created")
        else:
            print("A superuser already exists, not creating one")
