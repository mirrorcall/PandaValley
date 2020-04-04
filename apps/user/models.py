from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

# class Manager(models.Manager):
#     def get_queryset(self):
#         return super(Manager, self).get_queryset().filter(is_deleted=False)
#

class UserProfile(AbstractUser):

    GENDER_CHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    # Using CharField with RegexValidator simulating the filed for phones
    # It has to be exactly 10 digits
    telephone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    # File path for the avatar shall be stored
    avatar = models.FileField(upload_to='avatar', default='default_avatar.png')
    email = models.EmailField(primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    c_time = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email + " " + self.first_name + self.last_name + self.telephone + self.password


# class UserToken(models.Model):
#     """
#     Validate if user has been logged in.
#     """
#     user = models.OneToOneField(UserProfile, null=True)
#     token = models.CharField(max_length=64)
###
class WishList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    property = models.ForeignKey('property.Property', on_delete=models.CASCADE, primary_key=True)