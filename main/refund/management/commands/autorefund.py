from django.core.management.base import BaseCommand, CommandError
from refund.models import Master
import csv

class Command(BaseCommand):
    help = 'Refund owner\'s remain account balance'

    def add_arguments(self, parser):
        parser.add_argument('owner_list', nargs=1, type=str)

    def handle(self, *args, **options):

        business_ids = []
        with open(options['owner_list'][0], newline='') as f:
            reader = csv.reader(f)
            for x in reader : 
                #self.stdout.write(self.style.SUCCESS('Successfully get business_id:%s' % x))
                business_ids.append(x[0])

        
        
        #[TODO] Gather into one transaction??
        for business_id in business_ids : 
            try : 
                master = Master.objects.get(business_id=business_id)
            except : 
                raise CommandError('business_id "%s" does not exist' % business_id)

            #[TODO] Query to database and assertion check 
            # assert(Query.result==master.balance)

            before_balance = master.balance

            master.balance = 0
            master.save()

            #[TODO] Query to database and assertion check 
            # assert(Query.result==master.balance)

            self.stdout.write(self.style.SUCCESS('Successfully refund "%s" "%d" -> "%d"' % (master.business_id,before_balance,master.balance)))
        


