from django.db import models

class main(models.Model): 
   amenities = models.TextField(blank=True)
   specialists = models.TextField(blank=True)
   diagnostics = models.TextField(blank=True)

class news(models.Model): 
   title = models.TextField(blank=True)
   article = models.TextField(blank=True)
    
def __str__(self):
        return '%s ' % (self.title)
		

