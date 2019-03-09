from django.db import models

class doctor(models.Model):
  title = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='doctor/static/css')
  photoname = models.TextField() 
  name = models.TextField()
  information = models.TextField()
  
  def __str__(self):
        return '%s ' % (self.title)