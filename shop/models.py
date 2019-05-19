from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    store_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)


    def __str__(self):
        return self.full_name




# Create your models here.
