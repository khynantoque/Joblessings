from django.db import models

# Create your models here.

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add = True)
    salary = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title