
from django.db import models

# Create your models here.
#DataBase for ark_work
class admin_data(models.Model):
    SRN=models.AutoField
    title=models.CharField(max_length=50)
    image=models.ImageField(null=True)
    desc=models.TextField()
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
#dataBase for blog
class admin_blog(models.Model):
    SRN=models.AutoField
    title=models.CharField(max_length=100)
    images=models.ImageField(null=True)
    desc=models.TextField(blank=True)
    wide_desc=models.TextField()
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    