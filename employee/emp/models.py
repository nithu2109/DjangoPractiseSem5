from django.db import models

# Create your models here.
class emploee_details(models.Model):
    ename = models.CharField(max_length=30)
    eaddress = models.CharField(max_length=30)
    ejoin_dt = models.DateField()
    edept = models.CharField(max_length=30)

    class Meta:
        ordering = ["-ejoin_dt"]

    def __str__(self):
        return self.ename
