from django.db import models

class Quote(models.Model):
    id=models.IntegerField(primary_key=True)
    author=models.CharField(max_length=35)
    content=models.CharField(max_length=100)