from django.db import models


class Contact(models.Model):
    name = models.CharField('name', max_length=200, blank=False, null=False)
    email = models.EmailField('email', null=False, blank=False)
    message = models.TextField('message', null=False, blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
