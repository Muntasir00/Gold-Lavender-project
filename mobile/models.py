from django.db import models

class Mobile(models.Model):
    brand_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    jan_code = models.BigIntegerField()
    image = models.ImageField(upload_to='media/%m/',blank=True)
    
    def __str__(self):
        return self.brand_name
    
    
    
