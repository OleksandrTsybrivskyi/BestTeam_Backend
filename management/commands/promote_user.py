from django.core.management.base import BaseCommand
from core.models import User

class Command(BaseCommand):
    help = 'Додає або знімає право is_accessibility_user для вказаного користувача.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Імʼя користувача')
        parser.add_argument(
            '--remove',
            action='store_true',
            help='Зняти право замість додати'
        )

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        remove = kwargs['remove']

        try:
            user = User.objects.get(username=username)

            user.is_accessibility_user = not remove
            user.save()

            if remove:
                self.stdout.write(self.style.SUCCESS(
                    f'У користувача {username} забрано доступ як accessibility user.'
                ))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Користувач {username} тепер має доступ як accessibility user.'
                ))

        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Користувача з іменем {username} не знайдено'))
