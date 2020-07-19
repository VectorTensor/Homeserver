from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=400)
    sender= models.CharField(max_length=60)

    def ___str__(self):
        return f"{self.message_text} by {self.sender}"
       
        