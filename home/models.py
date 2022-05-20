from django.core.validators import validate_email
from django.db import models
from django.urls import reverse


class Support(models.Model):
    title = models.CharField(max_length=120,)
    email = models.EmailField(validators=[validate_email])
    body = models.TextField()



    @staticmethod
    def get_absolute_url():
        return reverse("store:home")

    def __str__(self):
        return self.title + ' | ' + str(self.email)
