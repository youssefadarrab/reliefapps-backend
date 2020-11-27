from django.db import models

# Create your models here.

class History(models.Model):
    HistoryId = models.AutoField(primary_key=True)
    HistoryLink = models.CharField(max_length=400)
    # VideoLink = str(VideoLink).replace("watch?v=", "embed/")
    HistoryTimestamp = models.CharField(max_length=400)

class Bookmark(models.Model):
    BookmarkId = models.AutoField(primary_key=True)
    BookmarkLink = models.CharField(max_length=400)
    # VideoLink = str(VideoLink).replace("watch?v=", "embed/")  
