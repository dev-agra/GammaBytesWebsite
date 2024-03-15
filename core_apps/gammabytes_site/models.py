from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    company = models.CharField(max_length=255, default='Null')