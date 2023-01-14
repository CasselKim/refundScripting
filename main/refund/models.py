from django.db import models

class Master(models.Model) : 
    business_id = models.CharField(max_length=11)
    balance = models.IntegerField(default=0)
    
# Create your models here.
