from django.db import models

# Create your models here.

class Bookmarks(models.Model):
    BookmarkId = models.AutoField(primary_key=True)
    BookmarkName= models.CharField(max_length=400)

class History(models.Model):
    HistoryId = models.AutoField(primary_key=True)