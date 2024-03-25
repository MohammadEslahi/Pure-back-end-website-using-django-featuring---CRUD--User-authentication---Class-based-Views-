from django.db import models
from django.urls import reverse

# Create your models here.
class trip(models.Model):
    destination = models.CharField(max_length=20)
    night = models.IntegerField()

    def __str__(self):
        return self.destination

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    
    