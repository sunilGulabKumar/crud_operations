from django.db import models

# Create your models here.
class HotelBook(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_location = models.CharField(max_length=100)
    # hotel_owner = models.CharField(max_length=100 )
    # hotel_restriction = models.BooleanField(default=False)
    # is_available = models.BooleanField(default=False)
    # charge = models.IntegerField(blank=True)
    # duration = models.DateTimeField(auto_now=True)