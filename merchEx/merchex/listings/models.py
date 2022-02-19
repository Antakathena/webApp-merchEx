from django.db import models

class band(models.Model):
    name = models.fields.CharField(max_length=100)

