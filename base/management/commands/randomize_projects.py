import django

django.setup()

from django.core.management.base import BaseCommand, CommandError
from base.models import User, Project
from base.helpers.sheet_randomizer import SheetRandomizer
import multiprocessing as mp

randomizer = SheetRandomizer()


def process_user(user):
    try:
        print(f"User: {user.username}")
        projects = Project.objects.filter(user=user.id)
        for project_idx, project in enumerate(projects):
            print(f"\tProject: {project_idx}. {project.name}")
            randomizer.update_sheet(project.sheet_id)
    except Exception as e:
        print('Error occured: ' + str(e))


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.filter(role=User.Role.ROLE_CUSTOMER)

        self.run_in_parallel([process_user] * len(users), users)

    def run_in_parallel(self, tasks: list, args: list):
        processes = [mp.Process(target=_task, args=(args[task_idx],)) for task_idx, _task in enumerate(tasks)]
        for running_task in processes:
            running_task.start()
        for running_task in processes:
            running_task.join()
