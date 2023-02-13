from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Site(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    order_id = models.IntegerField(null=False)
    purchase_id = models.CharField(max_length=100, null=False)

    csm_name= models.CharField(max_length=100, null=False)
    serial= models.CharField(max_length=100, null=False)
    ip_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    macaddr = models.CharField(max_length=100, null=False)
    
    

    def __str__(self):
        return str(self.order_id)