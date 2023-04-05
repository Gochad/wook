from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    textplace = models.TextField()
    add_time = models.DateField(auto_now=True)
