from django.core.management.base import BaseCommand, CommandError
from refund.models import Master
from random import randint

class Command(BaseCommand):
    help = 'Create owner objects'

    def add_arguments(self, parser):
        parser.add_argument('numbers', nargs='+', type=int)

    def handle(self, *args, **options):
        for _ in range(options['numbers']) :
            p = Master(business_id="{:03d}-{:02d}-{:04d}".format(randint(1,999),randint(1,99),randint(1,9999)), balance=randint(1,100000))
            p.save()
        self.stdout.write(self.style.SUCCESS('Successfully create %d objects' % (options['numbers'])))

        


