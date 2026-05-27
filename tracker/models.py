from django.db import models


class Shipment(models.Model):
    code = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=100)
    courier_name = models.CharField(max_length=100)

    def __str__(self):
        return self.code
