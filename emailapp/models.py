from django.db import models

class Email(models.Model):
    to_email = models.EmailField()
    from_email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
