from django.db import models

class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    name = models.CharField(max_length=100)
