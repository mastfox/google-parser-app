from django.contrib.sessions.models import Session
from django.db import models


class Parsers(models.Model):
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    position = models.IntegerField()
    update = models.DateTimeField()

    def __unicode__(self):
        return self.position

    class Meta:
        ordering = ["position"]


# result = Parsers(link='https://vironit.com/', position="1", update='2020-02-24 22:40')
# result.save()

# Create your models here.
