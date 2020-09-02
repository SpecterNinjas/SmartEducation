from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13)
    text = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created']
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us requests'
