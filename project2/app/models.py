from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Call(models.Model):
    caller = models.ForeignKey(User, related_name='calls_made', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='calls_received', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.caller} called {self.receiver}"