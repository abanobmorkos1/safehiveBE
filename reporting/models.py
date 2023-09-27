from django.db import models

class SafehiveDetails(models.Model):
    address = models.CharField(max_length=100)
    incident = models.CharField(max_length=100)
    emergency = models.BooleanField(default=False)
