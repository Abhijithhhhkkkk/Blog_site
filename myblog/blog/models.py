from django.db import models
import datetime
from django.utils import timezone
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def was_published_recently(self):
        return self.time >=timezone.now() -datetime.timedelta(days=1)
    def __str__(self):
        return self.title

# Create your models here.
