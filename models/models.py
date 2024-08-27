from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


called = 'called',
uncalled = 'uncalled',
recalled = 'recalled',
complete = 'complete',
rejected = 'rejected',

class Status(models.TextChoices):
    uncalled = uncalled
    called = called
    recalled = recalled
    complete = complete
    rejected = rejected




class Leeds(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = PhoneNumberField()
    comment = models.TextField(null=True, blank=True)
    objects = models.Manager()
    status = models.CharField(max_length=50, choices=Status, default=Status.uncalled)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} {self.phonenumber}'

