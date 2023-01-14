from django.core.management.base import BaseCommand, CommandError
from refund.models import Master
from random import randint

class Command(BaseCommand):
    help = 'Refund owner\'s remain account balance'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        
        '''
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        '''
        
        p = Master(business_id="{:03d}-{:02d}-{:04d}".format(randint(1,999),randint(1,99),randint(1,9999)), balance=randint(1,100000))
        p.save()
        self.stdout.write(self.style.SUCCESS('Successfully create objects "%s", %d' % (p.business_id, p.balance)))

        


