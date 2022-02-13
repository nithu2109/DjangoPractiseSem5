from django.db import models

# Create your models here.
class BusDetails(models.Model):
    Bus_No=models.IntegerField()
    Departure_Time=models.TimeField()
    Destinations=models.CharField(max_length=50)
    Seats_Available=models.IntegerField()
    TicketCosts=models.IntegerField()

class Ticket(models.Model):
    Bus_No=models.IntegerField()
    Destinations=models.CharField(max_length=50)
    No_of_Persons=models.IntegerField()
