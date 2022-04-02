from django.db import models

# Create your models here.
class word_Dict(models.Model):
    '''
    Word Models
    '''
    word=models.CharField(max_length=40)
