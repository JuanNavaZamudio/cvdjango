from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    addres = models.TextField(max_length=500)
    active = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.user.first_name + ", " + self.user.email

class Topic(models.Model):
    description = models.CharField(max_length=50)

class Message(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    message = models.TextField(max_length=2000)
    save_date = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.message
    

