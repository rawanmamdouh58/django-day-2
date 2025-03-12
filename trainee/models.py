from django.db import models

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, default='dina@gmail.com')
    image = models.ImageField(upload_to='trainee/img', default='dina.png')
    status = models.BooleanField(default=True)
