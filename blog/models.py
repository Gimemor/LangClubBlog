from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.TextField(default='')
    description = models.TextField(default='')
    post = models.TextField(default='')
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.post