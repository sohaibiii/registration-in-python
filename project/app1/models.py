from django.db import models
from django.contrib.auth.models import User   # built-in user model in django


# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional fields

    portfoliourl = models.URLField(blank=True)
    portfoliopic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username
