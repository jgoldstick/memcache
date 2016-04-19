from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible


from django.db import models
from django.contrib import admin

# Create your models here.


class Message(models.Model):
    state = models.CharField('State', max_length=64)
    city = models.CharField('City', max_length=64)
    username = models.CharField('User', max_length=64)
    message = models.TextField('Message')
    create_time = models.DateTimeField('Date', auto_now_add=True)

    def __unicode__(self):
        return "%s %s %s %s %s" % (self.username, self.city, self.state,
                                   self.message, self.create_time)

    class Meta:
        ordering = ('state', 'city', 'create_time')


class MessageAdmin(admin.ModelAdmin):
    fields = ('username', 'city', 'state', 'creation_time', 'message')
