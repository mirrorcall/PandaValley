from django.db import models

# Create your models here.

#from ..user.models import UserProfile
class Property(models.Model):
    #foreignkey
    #default id pk

    host_id = models.ForeignKey('user.UserProfile',on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    host_name = models.CharField(max_length=15)
    suburb = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    #x y on the google map
    latitude = models.FloatField()
    longitude = models.FloatField()
    property_type = models.CharField(max_length=15)
    description = models.TextField()
    # property state
    #avaiable = models.BooleanField(default=True)
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    single_bed = models.IntegerField(default=0)
    double_bed = models.IntegerField(default=0)
    queen_bed = models.IntegerField(default=0)
    king_bed = models.IntegerField(default=0)
    # 2 decimal place
    price = models.DecimalField(max_digits=8,decimal_places = 2)
    amenities = models.TextField()
    rating = models.DecimalField(max_digits=8,decimal_places = 2)
    cleaning_fee = models.DecimalField(max_digits=8,decimal_places = 2)
    # need change later on
    images = models.URLField()

    def __str__(self):
        return self.host_id + ' ' + self.host_name

class Booking(models.Model):
    host_id = models.ForeignKey(Property,on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest = models.ForeignKey('user.UserProfile',on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default = False)