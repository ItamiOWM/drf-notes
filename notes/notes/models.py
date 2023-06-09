from django.db import models

from accounts.models import User


# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, )
    content = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
