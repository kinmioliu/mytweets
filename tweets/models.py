from django.db import models
#from user_profile import User
from user_profile.models import User
# Create your models here.

class Tweet(models.Model):
    """
    Tweet model
    """
    user = models.ForeignKey(User)
    VISUAL_ABLE = (
        ('Y','YES'),
        ('N','NO'),
    )
#    is_visual = models.CharField(max_length=10, choices=VISUAL_ABLE)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
