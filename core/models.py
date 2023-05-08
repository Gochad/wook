from django.db import models
from authUser.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from wook import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Preference(models.Model):
    themes = (
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
    )

    preference_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=255, choices=themes)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='One Entry Per User')
        ]