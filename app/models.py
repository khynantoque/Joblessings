from django.db import models
from django.utils.text import slugify

# Create your models here.

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add = True)
    salary = models.IntegerField()
    expiry = models.DateField(null=True)
    slug = models.SlugField(null=True, max_length=40, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title