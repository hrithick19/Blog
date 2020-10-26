from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
import datetime

# Create your models here.
class kavithai(models.Model):
    kavithai_title=models.CharField(max_length=100)
    kavithai_content=HTMLField()
    image=models.ImageField(upload_to='Pictures/kavidhai')
    image_alt_text=models.CharField(max_length=100,default="alternate text")
    pub_date=models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=2)     
    def __str__(self):
        return self.kavithai_title
   

class kadhai(models.Model):
    kadhai_title=models.CharField(max_length=100)
    kadhai_description=models.CharField(max_length=300,default="No description available")
    kadhai_content=HTMLField()
    image=models.ImageField(upload_to='Pictures/kadhai')
    image_alt_text=models.CharField(max_length=100,default="alternate text")
    pub_date=models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=2)     
    def __str__(self):
        return self.kadhai_title

class katturai(models.Model):
    katturai_title=models.CharField(max_length=100)
    katturai_content=HTMLField()
    image=models.ImageField(upload_to='pictures/katturai')
    image_alt_text=models.CharField(max_length=100,default="alternate text")
    pub_date=models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=2)     
    def __str__(self):
        return self.katturai_title

