from django.db import models

class Author (models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        db_table = 'authors'
        
        
