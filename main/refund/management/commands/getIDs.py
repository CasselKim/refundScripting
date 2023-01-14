from django.core.management.base import BaseCommand, CommandError
from refund.models import Master
from random import randint

class Command(BaseCommand):
    help = 'get owner objects\'s business ids'

    def handle(self, *args, **options):
        for obj in Master.objects.all() :
            self.stdout.write('business_id : {}, balance : {}'.format(obj.business_id, obj.balance))

        


