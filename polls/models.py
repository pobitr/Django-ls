from django.db import models

# Create your models here.
class Con(models.Model):
	email = models.CharField(max_length=122)
	pwd = models.CharField(max_length=200)

   