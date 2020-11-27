from django.db import models

# Create your models here.

class Videos(models.Model):
    VideoId = models.AutoField(primary_key=True)
    VideoLink = models.CharField(max_length=400)
    # VideoLink = str(VideoLink).replace("watch?v=", "embed/")
    VideoTimestamp = models.CharField(max_length=400)
