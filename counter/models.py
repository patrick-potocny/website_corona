from django.db import models
from django.core.mail import send_mail

class Subscriber(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, error_messages={'unique': "This email is already registered."})

    #     Email sending

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail(
                'Thanks for suscribing ' + self.name,
                'Here is the message.',
                'patojezkopotocny@gmail.com',
                [self.email],
                fail_silently=False,
            )
        return super(Subscriber, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

