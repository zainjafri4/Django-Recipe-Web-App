from django.db import models

class rec(models.Model):
    rec_name = models.CharField(max_length=100)
    rec_dec = models.TextField()
    rec_image = models.ImageField(null=True, upload_to="rec_folder")
