from django.db import models
from django.utils import timezone

# Create your models here.
class Tache(models.Model):
    #id
    titre = models.CharField(max_length=100)
    details = models.TextField()
    date    = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titre
