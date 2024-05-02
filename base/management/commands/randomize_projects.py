import time

from django.core.management.base import BaseCommand, CommandError
from base.models import User, Project
from base.helpers.sheet_randomizer import SheetRandomizer


class Command(BaseCommand):
    def handle(self, *args, **options):
        randomizer = SheetRandomizer()
        users = User.objects.filter(role=User.Role.ROLE_CUSTOMER)
        for user_idx, user in enumerate(users):
            print(f"User: {user_idx}. {user.username}")

            projects = Project.objects.filter(user=user.id)
            for project_idx, project in enumerate(projects):
                print(f"\tProject: {project_idx}. {project.name}")
                randomizer.update_sheet(project.sheet_id)
                time.sleep(5)
