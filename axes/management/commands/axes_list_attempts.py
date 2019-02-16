from django.core.management.base import BaseCommand

from axes.models import AccessAttempt


class Command(BaseCommand):
    help = 'List access attempts'

    def handle(self, *args, **options):  # pylint: disable=unused-argument
        for obj in AccessAttempt.objects.all():
            self.stdout.write('{ip}\t{username}\t{failures_since_start}'.format(
                ip=obj.ip_address,
                username=obj.username,
                failures_since_start=obj.failures_since_start,
            ))
