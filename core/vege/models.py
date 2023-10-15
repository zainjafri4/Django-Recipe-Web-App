from django.db import models
from django.contrib.auth.models import User

class rec(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rec_name = models.CharField(max_length=100)
    rec_dec = models.TextField()
    rec_image = models.ImageField(null=True, upload_to="rec_folder")
