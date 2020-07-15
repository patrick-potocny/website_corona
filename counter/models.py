from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, error_messages={'unique': "This email is already registered."})

    def __str__(self):
        return self.email

