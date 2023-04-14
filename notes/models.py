from django.db import models
from django.urls import reverse
from core.models import User


class Note(models.Model):
    title = models.CharField(max_length=255)
    textplace = models.TextField()
    add_time = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])
