from django.contrib.sessions.models import Session
from django.db import models


class Parsers(models.Model):
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    position = models.IntegerField()
    update = models.DateTimeField()


# result = Parsers(link='https://vironit.com/', position="1", update='2020-02-24 22:40')
# result.save()

# Create your models here.
