from django.db import models

# Create your models here.


class Property(models.Model):
    """
    foreignkey
    default id pk
    """
    host = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)  # email
    title = models.CharField(max_length=50)
    host_name = models.CharField(max_length=15)
    suburb = models.CharField(max_length=15)
    street = models.CharField(max_length=30)
    postcode = models.CharField(max_length=4)
    room_type = models.CharField(max_length=10)
    # x y on the google map
    # latitude = models.FloatField(default=0)
    # longitude = models.FloatField(default=0)
    description = models.TextField(null=True)
    # property state
    # avaiable = models.BooleanField(default=True)
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    single_bed = models.IntegerField(default=0)
    double_bed = models.IntegerField(default=0)
    queen_bed = models.IntegerField(default=0)
    king_bed = models.IntegerField(default=0)
    num_review = models.IntegerField(default=0)

    # 2 decimal place
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # amenities = models.TextField()
    rating = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cleaning_fee = models.DecimalField(max_digits=8, decimal_places=2, default=50)
    # need change later on
    image = models.FileField(upload_to='images')
    imageUrl = models.URLField(null=True)

    def __str__(self):
        return str(self.host_id) + ' ' + str(self.host_name)


class Booking(models.Model):
    #property id
    host = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class Inspection(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')

