from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BookingInformation(models.Model):
    UserID = models.ForeignKey(User, on_delete = models.CASCADE)
    FromLocation = models.CharField(max_length = 100)
    ToLocation = models.CharField(max_length = 100)
    VehicalType = models.CharField(max_length = 100)
    PaymentMode = models.CharField(max_length = 100)
    DateAdded = models.DateTimeField(auto_now_add=True)