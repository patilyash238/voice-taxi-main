from django.contrib import admin
from . import models

class Booking(admin.ModelAdmin):
    list_display = ["UserID", "FromLocation", "ToLocation", "VehicalType", "PaymentMode"]
# Register your models here.
admin.site.register(models.BookingInformation, Booking)