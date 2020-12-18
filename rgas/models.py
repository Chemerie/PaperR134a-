from django.db import models

# Create your models here.


class Comment(models.Model):
	name = models.CharField(max_length=64)
	text = models.TextField()