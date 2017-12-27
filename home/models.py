from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
	mobile = models.CharField(max_length=15)
	name = models.CharField(max_length=50)
